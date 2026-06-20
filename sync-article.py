#!/usr/bin/env python3
"""
Sync an article from HFsourcing to the china-sourcing-guide knowledge base.

Usage:
  python3 sync-article.py <article-route-name>

Example:
  python3 sync-article.py golden-sample-china-manufacturing-quality-control

The article route name corresponds to the URL path and the TSX page directory
under src/app/(frontend)/<article-route-name>/
"""

import re
import sys
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

# Paths
HF_SOURCING = Path("/Users/hfsourcing/huangsourcing/HFsourcing")
KNOWLEDGE_BASE = Path("/Users/hfsourcing/china-sourcing-guide")
ARTICLES_DIR = KNOWLEDGE_BASE / "articles"
SRC_LIB = HF_SOURCING / "src" / "lib"
LOCAL_TZ = timezone.utc  # Will adjust to EDT below

BEIJING_OFFSET = timezone(datetime.now(timezone.utc).astimezone().utcoffset() + 
                          (lambda: __import__('datetime').timedelta(hours=8))() if False else 
                          datetime.now(timezone.utc).astimezone().utcoffset())

# Actually simpler - just use offset
from datetime import timedelta
BEIJING_TZ = timezone(timedelta(hours=8))


def slug_to_ts_file(slug: str) -> Path:
    """Convert article route slug to TypeScript data file path."""
    # Some articles use the route slug, some use a shorter name
    # Map known slugs to their TS filenames
    mapping = {
        "golden-sample-china-manufacturing-quality-control": "golden-sample-china-manufacturing-article.ts",
        "aql-inspection-china-sample-size-defect-limits": "aql-inspection-china-article.ts",
        "factory-vs-trading-company-signals": "factory-vs-trading-company-signals-article.ts",
        "qc-inspection-china-before-balance-payment": "qc-before-balance-article.ts",
        "supplier-verification-china-limits": "supplier-verification-china-limits-article.ts",
        "supplier-verification-vs-factory-audit": "supplier-verification-vs-factory-audit-article.ts",
        "forwarder-pickup-china-risks": "forwarder-pickup-china-risks-article.ts",
        "chinese-supplier-deposit-decision": "chinese-supplier-deposit-decision-article.ts",
        "amazon-fba-prep-china": "amazon-fba-prep-article.ts",
        "amazon-sellers-fba-prep-china": "amazon-sellers-fba-prep-china-article.ts",
        "buyer-side-inspection-report": "buyer-side-inspection-report-article.ts",
        "china-qc-inspection-booking-checklist": "china-qc-inspection-booking-checklist-article.ts",
        "fnsku-label-mistakes": "fnsku-label-mistakes-article.ts",
        "packaging-label-check-before-payment": "packaging-label-check-before-payment-article.ts",
        "pre-shipment-before-pickup": "pre-shipment-before-pickup-article.ts",
        "production-vs-pre-shipment-inspection": "production-vs-pre-shipment-inspection-article.ts",
        "sample-consolidation-china-compare-suppliers-before-choosing-factory": "sample-consolidation-compare-suppliers-article.ts",
        "alibaba-supplier-verification-payment": "alibaba-supplier-verification-payment-article.ts",
        "huang-sourcing-check-scope": "huang-sourcing-check-scope-article.ts",
        "china-factory-production-delays-timeline-management": "china-factory-production-delays-article.ts",
    }
    ts_name = mapping.get(slug)
    if ts_name:
        return SRC_LIB / ts_name
    # Try direct match
    direct = SRC_LIB / f"{slug}-article.ts"
    if direct.exists():
        return direct
    # Try as-is
    as_is = SRC_LIB / f"{slug}.ts"
    if as_is.exists():
        return as_is
    raise FileNotFoundError(f"Could not find article file for slug: {slug}")


def extract_value(text: str, key: str, multiline: bool = False) -> str:
    """Extract a simple string value from TypeScript source."""
    if multiline:
        # Multi-line string with backticks or quotes
        patterns = [
            rf"(?:^|,|\s){key}:\s*`([^`]+)`",
            rf"(?:^|,|\s){key}:\s*'([^']+)'",
            rf"(?:^|,|\s){key}:\s*\"([^\"]+)\"",
        ]
    else:
        patterns = [
            rf"(?:^|,|\s){key}:\s*'([^']+)'",
            rf"(?:^|,|\s){key}:\s*\"([^\"]+)\"",
        ]
    
    for pattern in patterns:
        m = re.search(pattern, text, re.MULTILINE)
        if m:
            return m.group(1)
    return ""


def extract_date(text: str) -> str:
    """Extract published date."""
    date = extract_value(text, "publishedDate")
    if date:
        return date
    return datetime.now(BEIJING_TZ).strftime("%Y-%m-%d")


def build_markdown(slug: str, ts_text: str, title: str, description: str, date_str: str, href: str) -> str:
    """Build a complete Markdown article from the TypeScript data."""
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"> Published: {date_str}")
    lines.append(f"> Original: https://www.huangsourcing.com{href}")
    lines.append("")
    
    # Description
    if description:
        lines.append(description)
        lines.append("")
    
    # Intro
    intro = extract_value(ts_text, "intro", multiline=True)
    if intro:
        lines.append(intro)
        lines.append("")
    
    # Quick checks / answer summary
    quick_answer = extract_value(ts_text, "answerSummary", multiline=True)
    if quick_answer:
        lines.append("## Quick Answer")
        lines.append("")
        lines.append(quick_answer)
        lines.append("")
    
    # FAQ section
    faqs = re.findall(r"\{\s*question:\s*'([^']+)'\s*,\s*answer:\s*'([^']+)'\s*\}", ts_text, re.DOTALL)
    if faqs:
        lines.append("## FAQ")
        lines.append("")
        for q, a in faqs:
            # Clean the answer text
            a = a.replace("\\n", "\n")
            lines.append(f"**Q: {q}**")
            lines.append("")
            lines.append(a)
            lines.append("")
    
    # Related links
    related = re.findall(r"href:\s*'([^']+)'\s*,\s*label:\s*'([^']+)'\s*,\s*note:\s*'([^']+)'", ts_text)
    if related:
        lines.append("## Related Guides")
        lines.append("")
        for href_val, label, note in related:
            lines.append(f"- [{label}](https://www.huangsourcing.com{href_val}) — {note}")
        lines.append("")
    
    # Topic tags
    tags = set()
    if "qc" in slug.lower() or "inspection" in slug.lower():
        tags.add("quality-control")
    if "supplier" in slug.lower() or "verification" in slug.lower() or "factory" in slug.lower():
        tags.add("supplier-verification")
    if "sample" in slug.lower() or "golden" in slug.lower():
        tags.add("sample-management")
    if "payment" in slug.lower() or "deposit" in slug.lower() or "balance" in slug.lower():
        tags.add("payment-and-release")
    if "pickup" in slug.lower() or "forwarder" in slug.lower() or "pre-shipment" in slug.lower():
        tags.add("shipping-and-logistics")
    if "amazon" in slug.lower() or "fba" in slug.lower() or "fnsku" in slug.lower() or "label" in slug.lower():
        tags.add("amazon-fulfillment")
    
    # Top matter
    top = f"---\ntitle: \"{title}\"\ndate: {date_str}\nsource: https://www.huangsourcing.com{href}\ntopics: [{', '.join(sorted(tags))}]\n---\n\n"
    
    return top + "\n".join(lines)


def sync_article(slug: str) -> dict:
    """Sync one article. Returns result dict."""
    ts_path = slug_to_ts_file(slug)
    if not ts_path.exists():
        return {"success": False, "error": f"File not found: {ts_path}"}
    
    ts_text = ts_path.read_text()
    
    # Extract metadata
    title = extract_value(ts_text, "title")
    if not title:
        # Try h1
        title = extract_value(ts_text, "h1")
    if not title:
        title = slug.replace("-", " ").title()
    
    description = extract_value(ts_text, "metaDescription")
    date_str = extract_date(ts_text)
    href = extract_value(ts_text, "href")
    if not href:
        href = f"/{slug}"
    
    # Build markdown
    md = build_markdown(slug, ts_text, title, description, date_str, href)
    
    # Write article
    md_path = ARTICLES_DIR / f"{slug}.md"
    md_path.write_text(md)
    
    # Update README index
    readme_path = KNOWLEDGE_BASE / "README.md"
    readme = readme_path.read_text()
    
    # Check if article is already in index
    if slug not in readme:
        # Find the "Contents" table and add entry
        entry = f"| | [{title}](articles/{slug}.md) | {date_str} |"
        # Insert after last table row
        lines = readme.split("\n")
        new_lines = []
        inserted = False
        for i, line in enumerate(lines):
            new_lines.append(line)
            if not inserted and line.startswith("*(Full index"):
                new_lines.insert(-1, entry)
                inserted = True
        if not inserted:
            new_lines.append(entry)
        readme_path.write_text("\n".join(new_lines))
    
    # Git commit
    try:
        subprocess.run(["git", "-C", str(KNOWLEDGE_BASE), "add", "."], check=True, capture_output=True)
        subprocess.run(
            ["git", "-C", str(KNOWLEDGE_BASE), "commit", "-m", f"Add article: {title}", "--author", "Huang Sourcing Bot <bot@huangsourcing.com>"],
            check=True, capture_output=True,
        )
        subprocess.run(["git", "-C", str(KNOWLEDGE_BASE), "push"], check=True, capture_output=True, timeout=30)
    except subprocess.CalledProcessError as e:
        return {"success": False, "error": f"Git error: {e.stderr.decode() if e.stderr else e}"}
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Git push timed out"}
    
    return {"success": True, "title": title, "path": str(md_path)}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: sync-article.py <article-route-name>", file=sys.stderr)
        sys.exit(1)
    
    slug = sys.argv[1]
    result = sync_article(slug)
    
    if result["success"]:
        print(f"✅ Synced: {result['title']} → {result['path']}")
    else:
        print(f"❌ Failed: {result.get('error', 'Unknown error')}", file=sys.stderr)
        sys.exit(1)