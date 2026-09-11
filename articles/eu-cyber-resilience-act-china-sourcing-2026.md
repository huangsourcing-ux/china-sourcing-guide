---
title: "EU Cyber Resilience Act: China Sourcing Checks"
date: 2026-07-08
updated: 2026-09-11
source: https://www.huangsourcing.com/eu-cyber-resilience-act-china-sourcing-2026
production_commit: cbdb0757b7bde53e2595a5bc309664884ccae3ea
author: Huang Sourcing Editorial Team
topics: [connected-products, quality-control, supplier-verification, shipping-and-logistics]
---

# EU Cyber Resilience Act: China Sourcing Checks

> Written by Huang Sourcing Editorial Team. Originally published by Agent Huang.
> Published: July 8, 2026 | Updated: September 11, 2026
> Original: https://www.huangsourcing.com/eu-cyber-resilience-act-china-sourcing-2026
> Production commit: https://github.com/huangsourcing-ux/huangsourcing/commit/cbdb0757b7bde53e2595a5bc309664884ccae3ea

CRA reporting starts September 11, 2026. Check manufacturer ownership, firmware, supplier escalation and shipment evidence before releasing connected products.

![Original diagram linking the shipment lot, responsible manufacturer and CRA reporting handoff; not documentary evidence of the TRENDnet case](https://www.huangsourcing.com/images/cra-reporting-handoff.webp)

From September 11, 2026, the EU Cyber Resilience Act requires manufacturers to report actively exploited vulnerabilities and severe incidents affecting in-scope products with digital elements. Its main product requirements apply from December 11, 2027. For buyers sourcing connected devices from China, the immediate decision is whether the exact shipment can be traced to a responsible manufacturer and a working supplier escalation route.

Dates: [Commission reporting guidance](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) · [CRA application timeline](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)

## Quick Answer

Before balance payment or pickup, match the model, hardware revision, firmware, app or cloud dependency and shipment lot to the approved product file. Name the manufacturer and the people who can assess security reports and obtain supplier fixes. Hold unexplained version substitutions or missing escalation ownership for review. A China-side inspection can record this evidence; it cannot establish cybersecurity compliance or decide whether an incident must be reported.

## Release Checklist

1. Record EU destination, connected functions and a qualified scope decision for each product family.
2. Identify the legal manufacturer, brand owner, importer and technical supplier; do not assume the factory is the manufacturer for CRA purposes.
3. Match the approved hardware, firmware, app and cloud dependencies to sampled production units and carton lots.
4. Name the manufacturer’s security decision-maker, reporting contact, backup and supplier engineering escalation contact.
5. Keep awareness timestamps, affected versions and correction records available to the responsible security team.
6. Separate the reporting duty applicable in September 2026 from the main CRA product requirements due in December 2027.
7. Escalate known security concerns immediately; a payment or shipment hold does not pause a reporting deadline.
8. Release only after the buyer and responsible specialists resolve identified gaps and accept the exact shipment evidence.

### Who owns the product?

- Brand and legal manufacturer identity, EU importer, technical supplier, firmware developer and cloud provider recorded in the order file.
- Named security escalation contacts and a backup route that works across supplier and buyer time zones.

### Which version is shipping?

- Model, hardware revision, firmware build, app version, relevant dependencies and lot references captured from accessible units.
- Approved reference file, sampled-unit identifiers and carton map make mixed or substituted versions visible.

### What happens after an alert?

- A documented path sends vulnerability information, affected versions and awareness times to the manufacturer’s security owner.
- The responsible team owns reportability decisions, reporting, patches and user communication; an inspector records evidence.

### What blocks release?

- Unexplained firmware changes, inaccessible version evidence, inconsistent labels or missing technical contacts trigger buyer review.
- Record the affected quantity, hold status, approved correction, specialist acceptance and re-check evidence.

## What applies now, and what waits until 2027?

The reporting start date has arrived. This update replaces the July planning guidance with a shipment handoff for the September 2026 reporting stage. The December 11, 2027 date remains the main application date for CRA product requirements; September 2026 is not a universal deadline for a CRA declaration of conformity or new CRA labelling.

Article 69 also brings products placed on the market before December 11, 2027 within Article 14 reporting. A buyer should therefore include existing EU product lines in the ownership discussion, not only the next purchase order. Keep any CE obligations that already apply under other legislation in the current release file.


References: [European Commission: CRA overview and timeline](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) · [EUR-Lex: Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng)

## Who reports when the factory and the brand are different?

Identify the manufacturer before asking who will file a report. The Commission describes the manufacturer as the person or organisation placing the product on the market under its name or trademark. A private-label buyer may therefore carry manufacturer responsibilities even when another business designs or assembles the device.

Ask the responsible team to confirm roles in writing. The sourcing file should show the company identity and the contacts who can reach the firmware developer, assess an alert, approve a fix and communicate with customers. A supplier promise to “handle compliance” is too vague to explain who acts when a security issue appears.

- Name the security owner and backup; record an escalation route for weekends and supplier holidays.
- Agree how the supplier will identify affected hardware and firmware versions and return correction evidence.
- Treat supplier response targets as commercial arrangements; they do not replace the manufacturer’s legal deadlines.

References: [European Commission: CRA legislative summary](https://digital-strategy.ec.europa.eu/en/policies/cra-summary)

## What are the CRA reporting deadlines?

For an actively exploited vulnerability or a severe incident, the manufacturer must issue an early warning without undue delay and within 24 hours of awareness, followed by a notification within 72 hours. For an actively exploited vulnerability, the final report is due no later than 14 days after a corrective or mitigating measure becomes available. For a severe incident, it is due within one month after the 72-hour notification.

These are event-reporting clocks, not shipment-document deadlines. Not every bug or failed inspection is reportable. The responsible security team must assess the event against the legal criteria. A sourcing team should preserve when information arrived, which versions may be affected and whom it notified; it should not wait for a complete inspection report before escalating a credible concern.


References: [European Commission: CRA reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) · [EUR-Lex: Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng)

## What should the manufacturer prepare for the reporting platform?

ENISA’s launch FAQ says Assigned Representatives use personal EU Login accounts with multi-factor authentication. Prepare the contact and access route, but do not require an advance SRP registration certificate from every supplier: ENISA advises initiating registration when a notification is needed. At launch, reporting uses the platform interface; there is no reporting API.

The launch supports mandatory manufacturer reports. Voluntary reporting is deferred, and open-source software steward reporting starts December 11, 2027. ENISA also distinguishes awareness before September 11, 2026 from awareness after that date; an older vulnerability can still trigger reporting when active exploitation becomes known later.

For the buyer, the useful deliverable is a named owner and a reliable technical handoff. Do not collect personal login credentials or file dummy incidents to test a supplier. Let the responsible manufacturer follow ENISA’s current registration and notification instructions.


References: [ENISA: Single Reporting Platform FAQ](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)

## How do you connect firmware evidence to the cartons?

Use one version register for the approved reference and the shipment. Record SKU, hardware revision, firmware build, app version, relevant remote service and the date of observation. Capture version screens only through access the supplier and buyer authorise. Link the photographs and observations to sampled serial numbers or lot identifiers.

An unchanged enclosure or barcode does not explain a firmware substitution. If the factory updates units after inspection, ask which quantities changed and obtain a new version list. Where a version cannot be read, record that limit. The buyer should decide with its technical owner whether further access, engineering review or re-inspection is needed before release.

- Sample across identified lots and record coverage; do not imply every device was checked.
- Compare labels, manuals, pairing instructions and QR destinations with the approved product file.
- Segregate unexplained variants and document any approved correction before revising the release decision.

## What belongs in the 2027 product-readiness file?

Plan separately for the main CRA requirements: cybersecurity risk assessment, technical documentation, conformity assessment, an EU declaration of conformity, CE marking and support information. A qualified owner should confirm product scope, any important or critical category, applicable exclusions and the conformity route. The Commission’s summary explains these product obligations.

For sourcing, keep a file index and revision history so that future technical documents describe the device actually ordered. Existing radio, electrical-safety, battery or other product rules may already require evidence. A CE logo or generic laboratory report cannot by itself answer whether the software, support process or CRA conformity plan is adequate.


References: [European Commission: CRA legislative summary](https://digital-strategy.ec.europa.eu/en/policies/cra-summary) · [European Commission: CRA overview and timeline](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)

## Public case example: TRENDnet connected cameras

What happened: in February 2014, the U.S. Federal Trade Commission approved a final order settling charges against TRENDnet. The FTC alleged that cameras marketed as secure contained software flaws that exposed private video feeds. The settlement required a security programme, independent assessments and customer notification about corrective software updates.

Public evidence: the FTC announcement and case docket contain the complaint and order. Buyer lesson: a functioning camera and a matching retail box cannot establish secure software or a workable customer-update process. The shipment record needs a usable link between the device version and the people responsible for security and fixes.

Limits: this older U.S. settlement is not a CRA enforcement decision, a finding about Chinese factories, or evidence that a current supplier has the same fault. It remains relevant because version identification and update communication are still practical sourcing handoff problems. Huang Sourcing did not participate in this case.


References: [FTC: final TRENDnet settlement order announcement](https://search.ftc.gov/news-events/news/press-releases/2014/02/ftc-approves-final-order-settling-charges-against-trendnet-inc) · [FTC: TRENDnet case docket and order](https://search.ftc.gov/legal-library/browse/cases-proceedings/122-3090-trendnet-inc-matter)

## Evidence to Decision Matrix

| Risk node | Evidence | Buyer decision |
| --- | --- | --- |
| Version and ownership evidence agree | Sampled units match the approved version file; the manufacturer and technical escalation contacts are named; responsible specialists accept the handoff. | Approve the documented sourcing release, subject to the buyer’s other product and destination checks. |
| Firmware differs or cannot be identified | Mixed builds, unexplained substitutions or inaccessible version information prevent a reliable lot match. | Hold affected quantities; request engineering review, an updated lot map and proportionate re-checks. |
| No manufacturer or reporting owner is clear | Brand, factory and importer redirect responsibility without an agreed legal role and technical contact. | Pause release while the responsible parties resolve ownership. Supplier labels alone do not settle legal status. |
| A security concern is already known | The order team receives a credible alert or version-specific security concern. | Escalate immediately to the manufacturer’s security team; preserve evidence and let qualified owners decide reporting and corrective action. |
| Only the future CRA conformity file is pending | A CRA-specific 2027 document is unavailable, while current reporting and other applicable requirements have been assessed. | Obtain a dated readiness plan; do not describe September 2026 as a blanket CRA CE-document deadline. |

## Research and Evidence Basis

- Public-source research checked September 11, 2026: European Commission guidance, ENISA platform FAQ, the CRA legal text and FTC records.
- The release checklist and decision matrix are Huang Sourcing editorial analysis applying those records to product identity and supplier handoffs.
- No private analytics, customer case files, first-hand inspection findings or supplier security assessments were used to write this update.
- A future order check needs buyer-provided references and explicitly recorded physical sampling; the examples here do not document an actual shipment.

## What to Send

- Product list, EU destinations, intended functions, brand, manufacturer, importer and qualified scope notes.
- Approved hardware and firmware register, app and relevant cloud dependencies, labels, manuals and product-file revision dates.
- Supplier and technical-provider contacts, manufacturer security owner, backup and agreed escalation route.
- Order quantity, production lots, serial ranges where available, carton map and payment or pickup deadline.
- Known changes or alerts, affected versions, approved corrections and specialist release instructions; exclude passwords and unnecessary personal information.

## Red Flags

- The supplier changes firmware or app pairing after the approved sample without a revision record.
- The brand owner, factory and importer cannot agree who is the manufacturer or who receives vulnerability reports.
- The same SKU contains different hardware or firmware and cartons do not identify the variants.
- Generic CE or test documents are presented as proof of software security or reporting readiness.
- A supplier asks the inspection team to defer a known security concern until the payment discussion is finished.

## Scope Limits

- Huang Sourcing can compare accessible device, version-screen, label, packaging, carton and supplier-document evidence against buyer-approved references in China.
- Cybersecurity testing, CRA legal scope, economic-operator classification, conformity assessment and reportability decisions require the responsible operators and qualified specialists.
- Sampling, inaccessible firmware, locked apps, unavailable technical files and supplier refusals must be recorded as evidence limits.
- A matched shipment file does not prove the absence of vulnerabilities, guarantee compliance or remove manufacturer reporting obligations.
- Platform procedures and product guidance can change. The responsible reporting team should consult the current official instructions when an event occurs.

## Sources

- [European Commission: CRA reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) — Official start date, reportable events, notification windows and reporting channel.
- [ENISA: Single Reporting Platform FAQ](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions) — Launch guidance checked September 11, 2026: assigned representatives, EU Login, legacy products and initial platform capabilities.
- [European Commission: CRA legislative summary](https://digital-strategy.ec.europa.eu/en/policies/cra-summary) — Product scope, manufacturer identity, economic operators and the main product-conformity requirements.
- [EUR-Lex: Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng) — Binding text, including Article 14 reporting, Article 69 transitional provisions and Article 71 application dates.
- [FTC: final TRENDnet settlement order announcement](https://search.ftc.gov/news-events/news/press-releases/2014/02/ftc-approves-final-order-settling-charges-against-trendnet-inc) — February 7, 2014 public record of allegations, security-program requirements and customer software-update notification.
- [FTC: TRENDnet case docket and order](https://search.ftc.gov/legal-library/browse/cases-proceedings/122-3090-trendnet-inc-matter) — Primary case file containing the complaint and decision and order; this was a U.S. FTC matter, not CRA enforcement.
- [European Commission: CRA overview and timeline](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) — September 11, 2026 reporting and December 11, 2027 main application dates.

## Related Guides

- [Pre-shipment inspection in China](https://www.huangsourcing.com/china-pre-shipment-inspection) — Plan the physical and documentary checks before cartons leave the supplier.
- [Before balance payment checklist](https://www.huangsourcing.com/before-balance-payment-qc-china) — Agree which evidence gaps block release and who can approve corrections.
- [Packaging and label checks before payment](https://www.huangsourcing.com/packaging-label-check-before-payment) — Connect product identifiers, manuals and cartons to the approved file.
- [Buyer-side inspection report guide](https://www.huangsourcing.com/buyer-side-inspection-report) — Record sampling, evidence limits and decisions clearly.
- [China sourcing risk guides](https://www.huangsourcing.com/china-sourcing-risk-guides) — Find related supplier, inspection and shipment decisions.
- [Free China sourcing risk check](https://www.huangsourcing.com/free-china-sourcing-risk-check) — Send the order stage, product details and unresolved evidence gaps.

## Frequently Asked Questions

### Does an ordinary QC inspection prove CRA compliance?

No. A QC inspection can record accessible product identity, versions, labels and documents. Cybersecurity engineering, conformity and reporting decisions sit with responsible operators and qualified specialists.

### Should a buyer demand a CRA certificate for every September 2026 shipment?

Do not turn the September reporting date into a blanket CRA certificate requirement. Establish current reporting ownership and applicable product-rule evidence, then agree a separate plan for the main CRA requirements applying in December 2027.

### What if the factory patches devices after inspection?

Ask for the affected quantity, old and new versions, correction approval and updated lot map. Have the technical owner assess the change and define the additional checks needed before releasing those units.

