# Service Contract for Development on Software Projects  

- A list of changes can be found [here](https://github.com/Osiris-Team/Osiris-Team/commits/main/dev_contract.md).  
- This file can be viewed as a raw text file [here](https://raw.githubusercontent.com/Osiris-Team/Osiris-Team/main/dev_contract.md).  
- This contract can be transformed into a .pdf [here](https://md2pdf.netlify.app/) or into .docx/.odt (word document) [here](https://www.vertopal.com/en/convert/md-to-odt).  

## 1. Applicable Parties  

| Identifier  | Full Name | Address | Github ID |  
| ----------- | ----------- |----------- | ----------- |  
| The Client / Client | _INSERT_ | _INSERT_ | _INSERT_ |  
| The Developer / Developer | Arman Ruben Kandel | Taunusstraße 124, 41236 Mönchengladbach, Germany | Osiris-Team |  

## 2. Variables  

### 2.1 Effective date: _INSERT_  
### 2.2 Selected payment package, hourly rate and currency: _INSERT_ (Basic, Pro or Expert), _INSERT_ ($80/h), _INSERT_ (USD, EURO, etc)
### 2.3 Selected payment logic: _INSERT_ (Prepaid, Postpaid, FPW Subscription or FP Subscription)  
### 2.4 Selected copyright terms: _INSERT_ (MIT License, Custom License, Copyright transfer)  

## 3. Validity  

- **3.1 Agreement:** All parties have freely agreed to the following and look forward to working together.  
- **3.2 Duration:** This contract is intended to be valid from acceptance by all parties until termination.
- **3.3 Superseding Clause:** Any previous versions of this contract are superseded upon mutual acceptance and transmission of a dated signed copy.  
- **3.4 Entire Agreement:** This contract constitutes the entire understanding between the parties and supersedes all prior agreements or understandings, whether written or oral. Any amendments to this contract must be in writing and signed by both parties. 
- **3.5 Severability:** If any provision of this contract is held to be invalid, illegal, or unenforceable under applicable law, the remaining provisions of this contract shall remain in full force and effect. The parties agree to replace the invalid, illegal, or unenforceable provision with a valid provision that most closely reflects the original economic and legal intent of the parties.

## 4. Governing Law and Dispute Resolution  

**4.1 Governing Law:** This Agreement shall be governed by and construed in accordance with the laws of Germany, excluding its conflict of law rules and the United Nations Convention on Contracts for the International Sale of Goods (CISG).

**4.2 Good Faith Negotiation:** In the event of a dispute, controversy, or claim arising out of or relating to this Agreement, the Parties shall first seek to resolve the matter through good faith negotiations, initiated by written notice describing the issue in reasonable detail. The recipient shall respond within ten (10) calendar days. Negotiation efforts must continue for a minimum of fifteen (15) calendar days from the date of initial notice.  

**4.3 Mediation:** If the matter remains unresolved after the negotiation period, either Party may submit the dispute to mediation. Mediation shall be administered by one of the following institutions, selected by mutual agreement:  
- World Intellectual Property Organization (WIPO) Arbitration and Mediation Center,  
- International Chamber of Commerce (ICC),  
- International Centre for Dispute Resolution (ICDR),  
- Or another internationally recognized institution.  
If the Parties cannot agree on an institution within ten (10) calendar days, WIPO shall serve as the default mediation body. Mediation shall be conducted in English, unless otherwise agreed.  

**4.4 Binding Arbitration and Standard Court Option:** If the mediation does not result in a resolution within thirty (30) calendar days following the appointment of a mediator, the dispute shall be resolved by binding arbitration under the applicable commercial rules of the selected institution. Arbitration shall be:  
- Conducted in English, unless otherwise agreed;  
- Decided by a single, neutral arbitrator jointly selected by the Parties;  
- Held with the seat of arbitration in Moenchengladbach, Germany, or another mutually agreed neutral location (including remote proceedings via videoconference, where appropriate).  
Judgment upon the arbitration award may be entered in any court of competent jurisdiction. The arbitration award shall be final and binding on both Parties.  
*Exception for Small Claims:* Notwithstanding the arbitration requirement above, either Party may bring an action in the standard local courts of Moenchengladbach, Germany, for any dispute or claim where the total amount in controversy is less than €10,000 (ten thousand Euros), excluding interest and costs.

**4.5 Interim Relief:** Either Party may seek interim, emergency, or injunctive relief in any court of competent jurisdiction when necessary to prevent irreparable harm, protect intellectual property, or preserve legal rights pending the resolution of the dispute. This right does not waive or limit the obligation to arbitrate.  

**4.6 Costs and Fees:** Each Party shall initially bear its own legal fees and costs associated with dispute resolution. However, the arbitrator shall have the discretion to allocate costs and reasonable attorneys’ fees in proportion to each Party’s success on the merits and the conduct of the Parties during the proceedings, including any finding of bad faith, procedural abuse, or failure to negotiate in good faith.  

## 5. Good Faith and Notice  

- The Developer will act in good faith (i.e. will not attempt deception or defraud via methods including but not limited to double billing of hours or making unnecessary code changes).  
- Any potential breach of good faith will lead to a discussion before exploring other options.  

## 6. Scope of Work  

**6.1 Task List:** The Developer will receive a list of tasks consisting of, for example, feature requests or bug fixes.  

**6.2 Task Clarity:** These tasks must be clear and concise. The Client must respond to the Developer’s questions if anything is unclear.  

**6.3 Task Rejection:** The Developer may reject one or more tasks but must provide a clear and concise reason. If the Developer rejects a task after starting work, the associated time must not be billed.  

**6.4 Task Priority:** The Developer shall propose the order, priority, and selection of tasks to be undertaken and delivered. The Client shall have the right to review and approve this proposed prioritization. Final task prioritization shall be mutually agreed upon, provided that such decisions do not conflict with any previously agreed-upon deadlines or priority arrangements.  

**6.5 Task Change:** The Client may propose changes or new tasks in writing. The Developer shall promptly estimate the impact on the required work hours, and the parties will mutually agree in writing before proceeding. Any material change in the scope or requirements of a task after work has begun must be documented in writing and approved by both parties, including any adjustment to the estimated hours, timeline, or deliverables.

**6.6 Delivery:** All completed tasks must be delivered by the Developer in one of the following ways, depending on who owns or maintains the repository:  

  1. When the Client or a Third-Party created or owns the repository:  
     - The Developer must submit the task as a separate Merge Request (MR) to the Client’s upstream repository (or fork), using a descriptive branch name and meaningful commit messages.  
     - For simplicity, the Developer might also ask for permission to instead create a single MR containing multiple tasks.  
     - Alternatively, if the Client uses an upstream public repository owned by another party, the Developer may submit a separate MR to the upstream repository, with the Client copied or tagged.  

  2. When the Developer created or owns the repository:  
     - The Developer may push changes as a commit to their own repository.  
     - The Client is responsible for creating a fork, cloning the repository, or exporting the work to integrate it into their environment.  

**6.7 Delivery Frequency:** The amount and frequency of deliveries is at the sole discretion of the Developer.  

**6.8 Delivery Labeling:** All deliveries must be clearly labeled and must reference the original tasks or issues they are intended to fulfill. The Client is responsible for testing whether the delivery fulfills the task requirements during the Post-Delivery Review Period.  

**6.9 Delivery Notification:** The Client must be notified about a delivery in writing or via electronic communication, and the notification must include a link to the MR or commit, along with a log of the hours worked on that specific delivery.  

**6.10 Delivery Usage and Testing:** The Client assumes all responsibility for use, deployment, and integration of the delivery in production systems, including proper testing, security, and compliance.  

**6.11 Post-Delivery Revisions:** The Client may request revisions or adjustments to a delivered task. Additional work or modifications requested by the Client that deviate from, or expand upon, the originally agreed task requirements constitute new efforts and shall be billed at the standard hourly rate. However, any work required to correct a defect or failure to meet the originally agreed specifications is governed by the Functionality Warranty (Section 6.14) and shall not be billed.  

**6.12 Hourly Billing on Delivery:** This Agreement is structured as an hourly-based service contract. All hours worked by the Developer on a task are directly billable or deductible from prepaid hours immediately upon delivery of the task (as defined in Section 6.6) and notification to the Client. Payment for the hours worked is tied solely to the completion and delivery of the task, and is not conditional upon prior review, testing, or formal acceptance by the Client.  

**6.13 Post-Delivery Review Period:** The Client has up to ninety (90) calendar days from the date of delivery to review, test, and integrate the submitted work. During this period, the Client may notify the Developer in writing of any defects, functional errors, or failures to meet the agreed-upon task specifications, which shall then be addressed under the Functionality Warranty.  

**6.14 Functionality Warranty and Defect Correction:** Notwithstanding the hourly service nature of this contract, the Developer warrants that the delivered work product will operate in accordance with the agreed-upon specifications for a period of ninety (90) calendar days following its delivery. If the Client identifies and reports a defect or failure to conform to specifications within this timeframe, the Developer shall, at their own expense (without billing additional hours) and within a reasonable timeframe, correct or replace the non-conforming software to ensure compliance. If the Developer is unable or declines to correct the non-conforming work within a reasonable timeframe, the Developer shall instead provide a refund for the hours directly billed for the affected task.  

**6.15 Exclusions:** The warranty does not cover issues arising from, and a refund is not possible when:  
- Modifications or alterations were made to the delivery by anyone other than the Developer.  
- The affected parts of the delivery have been materially modified.  
- The Client performed misuse, negligence, or unauthorized use of the delivery.  
- Environmental factors or hardware malfunctions that are not under the Developer's control.  

**6.16 Exclusive Remedy:** The remedies provided in this section (free defect correction or, alternatively, a refund of billed hours) are the Client's sole and exclusive remedies for any breach of the warranty.  

**6.17 Refund Amount:** The refund amount shall be calculated based on, and limited to, the number of hours directly attributable to the affected task at the time of delivery, multiplied by the applicable hourly rate in effect at that time.  

**6.18 Refund Finality:** Once a refund is issued, the Developer has no further obligations for the refunded task, and the Client waives future claims related to that task. 

**6.19 Dispute Resolution:** Both parties agree to first attempt resolution via good faith negotiation before escalating to mediation, arbitration, or legal action.

## 7. Timing  

- Time not spent actively working on a task (e.g., research, writing, or committing code) is the Developer's to use as they see fit.  
- The Developer can multitask at their complete discretion.  
- There is no rigid daily working schedule required of the Developer, allowing for a healthy study/life/work balance. However, this flexibility does not relieve the Developer of the obligation to meet the minimum weekly guaranteed hours of the selected package (Section 13), provided there are pending tasks to complete.

## 8. License and Copyright  

This section outlines multiple licensing models and copyright arrangements applicable to the Work Product delivered under this Agreement.  

**8.1 Selection Requirement:** One (1) of the sub-sections listed below (Sections MIT License, Custom License, Copyright transfer) must be explicitly selected and agreed upon in writing by both parties. Once selected, the remaining subsections shall be deemed inapplicable and without legal effect for the purposes of this Agreement.  

Each sub-section governs the Client’s and Developer’s rights, obligations, and limitations regarding use, modification, and ownership of the Work Product. The selected model shall override any conflicting provisions elsewhere in this Agreement, except where otherwise explicitly stated.  

### 8.2 MIT License  

Copyright 2025 Arman Ruben Kandel (Osiris-Team)  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

### 8.3 Custom License  

Copyright 2025 Arman Ruben Kandel (Osiris-Team)  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  

All software, code, documentation, designs, and other materials created under this Agreement (collectively, the "Work Product") will remain the intellectual property of the Developer.  

Upon full payment and acceptance of a task, the Client is granted an exclusive, perpetual, worldwide, royalty-free license to use, modify, reproduce, display, distribute, and create derivative works of the Work Product at the state it existed upon delivery, for any purpose, including commercial use.  

The Developer shall not reproduce, license, or distribute the Work Product, or any substantially similar derivative, to any third party. The Client has full practical control of the Work Product as if it were their own, except for claiming original authorship or asserting copyright ownership.  

### 8.4 Copyright Transfer  

**8.4.1 Transfer of Ownership:** Upon full payment and written acceptance of each individual delivery or milestone, the Developer agrees to transfer all rights, title, and interest, including copyright, in the specific Work Product delivered under that milestone (including all software, code, documentation, designs, and related materials) to the Client. Upon such transfer, the specified Work Product shall become the exclusive property of the Client in the form it existed at the time of delivery and acceptance.  

*Clarification for Cumulative Workflows:*  
If a subsequent deliverable (e.g., Deliverable #2) includes modifications, extensions, or enhancements to a previously accepted deliverable (e.g., Deliverable #1), the copyright and ownership of those new changes remain with the Developer until full payment and formal acceptance of the new deliverable are complete, even though they build upon software the Client already owns.  
Therefore, while the Client owns the previously accepted and paid-for base software (Deliverable #1), they do not acquire ownership of any subsequent additions, refinements, or alterations (Deliverable #2) until those specific elements are paid in full and accepted.  
*Use Limitation:* The Client may not use, reproduce, or incorporate any unaccepted or unpaid modifications into their systems or redistribute them, as doing so would violate the Developer’s retained copyright.

**8.4.2 Developer License:** To facilitate continued development, the Client grants the Developer a temporary, non-exclusive, non-transferable license to use, modify, and access the Work Product. This license is valid only while this contract remains active and un-terminated. The license exists solely for the purpose of completing ongoing or future Deliveries under this Agreement. Upon termination of this contract for any reason, this license is immediately revoked, and the Developer agrees to cease all use of the Work Product unless otherwise agreed in writing. Notwithstanding the foregoing, the Client reserves the right to revoke this license at its sole discretion at any time during the term of this Agreement, provided that such revocation does not conflict with any previously agreed-upon deadlines or priority arrangements.  

**8.4.3 Developer Restrictions:** The Developer agrees not to reproduce, license, or distribute the Work Product, or any substantially similar derivative, to any third party.  

**8.4.4 Use of Third Party and Open-Source Software:** The Developer may use third-party and/or open-source software components as part of the deliverables. The Developer shall:  
- Disclose all open-source software libraries used.  
- Ensure that all third-party components comply with licenses that allow commercial use, modification, and redistribution.  

**8.4.5 Third-Party Licensing Fees and Expenses:** The Client is solely responsible for obtaining and paying for any third-party commercial software licenses, API usage costs, subscriptions, hosting services, or infrastructure costs required to develop, build, test, deploy, or run the Work Product, unless otherwise agreed upon in writing.

**8.5 Intellectual Property Warranty:** The Developer represents and warrants that, to the best of their knowledge, the custom Work Product delivered under this Agreement is original and does not infringe upon any third-party intellectual property rights.

## 9. Background Technology  

**9.1 Developer Ownership:** Any pre-existing tools, components, or libraries developed by the Developer prior to or outside the scope of this agreement remain the property of the Developer.  

**9.2 Client License:** The Developer grants the Client a non-exclusive, perpetual, worldwide, and royalty-free license to use, modify, and distribute any Developer-owned Background Technology incorporated into the Work Product, solely as necessary for the use and operation of the Work Product as delivered.  

This license does not apply to any Background Technology or component that is governed by an existing license (including third-party open-source software), which shall apply in accordance with its own terms. The Developer represents and warrants that all such components will be clearly disclosed and properly attributed at the time of delivery.  

**9.3 Developer Use:** The Developer retains the right to use Background Technology for other projects, provided it does not infringe upon the Client's rights in the Work Product developed.  

**9.4 Survival of Terms:** The provisions of this section shall survive the termination or expiration of this Agreement.  

## 10. Limitations of Liability  

**10.1 Disclaimer of Warranties:** Except as expressly provided in the "Scope of Work" and "License and Copyright" sections of this Agreement, all software, source code, documentation, and other deliverables (collectively, the “Work Product”) are provided “AS IS”, without any warranties of any kind—whether express, implied, statutory, or otherwise. This includes, but is not limited to, implied warranties of merchantability, fitness for a particular purpose, non-infringement, or warranties arising from a course of dealing, usage, or trade practice.  

**10.2 Exclusions and Caps:** Subject to Section 10.3 and to the fullest extent permitted under applicable law:  
- The Developer shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including, but not limited to, loss of profits, loss of data, business interruption, or loss of business opportunities, even if the Developer has been advised of the possibility of such damages.  
- The Developer’s total cumulative liability under this Agreement shall not exceed the total fees actually paid by the Client for the specific task or deliverable giving rise to the claim.  
- The Developer’s liability for any breach of warranty is strictly limited to the correction or replacement of the non-conforming Work Product, as outlined in the "Scope of Work" section.  
- Third-party or open-source components incorporated into the Work Product are subject to their respective licenses, which may include “AS IS” disclaimers. The Client acknowledges and accepts the terms of such licenses and understands that the Developer does not provide any additional warranties for third-party or open-source software beyond compliance with license terms and proper attribution.  

**10.3 Legal Exceptions:** 
Notwithstanding any other provision in this Agreement, the limitations and exclusions of liability in this Section 10 shall not apply to, and nothing in this Agreement shall exclude or limit, the Developer’s liability for:

- Damages arising from injury to life, body, or health resulting from a negligent or intentional breach of duty by the Developer, or their legal representatives or vicarious agents;
- Intentional misconduct or gross negligence of the Developer, their legal representatives, or senior executives;
- Mandatory statutory liability under the German Product Liability Act, solely to the extent legally mandatory and applicable to software services;
- Claims based on fraudulently concealed defects or a specific guarantee of quality, if explicitly agreed upon in writing.

For damages caused by the simple or gross negligence of ordinary vicarious agents who are not legal representatives or senior executives of the Developer, the Developer's liability shall be strictly limited to the contract-typical, foreseeable damage as defined below.

In the case of a simple negligent breach of an essential contractual obligation, the Developer’s liability shall also be limited strictly to the contract-typical, foreseeable damage. For the purposes of this Agreement, an "essential contractual obligation" is narrowly defined as a duty whose fulfillment is absolutely essential to the proper execution of this contract and on whose compliance the Client may routinely rely (specifically, the primary service obligation to deliver functional code under the hourly structure). 

The Parties mutually agree that the contract-typical, foreseeable damage under this Agreement shall in no event exceed:
1. The total cumulative fees actually paid by the Client to the Developer under this Agreement during the twelve (12) months preceding the event giving rise to the claim, or
2. A maximum cumulative limit of €25,000 (twenty-five thousand Euros),
whichever amount is lower. This limit constitutes the Parties’ mutual pre-estimation of the maximum foreseeable damage typical for this type of software service contract.

## 11. Data Protection and Confidentiality

**11.1 Data Protection:** If the Work Product or services involve processing of personal data, the Developer agrees to comply with all applicable data protection laws, including the EU General Data Protection Regulation (GDPR), to the extent applicable. Client remains the Data Controller; Developer acts as Data Processor.  
The Developer shall do so only on documented instructions from the Client and in compliance with applicable data protection laws, including the EU General Data Protection Regulation (GDPR). The Developer shall implement appropriate technical and organizational measures to protect personal data against unauthorized access, loss, or breach. The Developer further agrees to sign a separate Data Processing Agreement, as required by GDPR Article 28, outlining the processor obligations, the nature of data processed, duration, and purpose of processing. The Developer will not transfer any personal data to a country outside the European Economic Area without ensuring adequate safeguards as required by GDPR (such as Standard Contractual Clauses or an approved transfer mechanism). The Developer also agrees to promptly inform the Client of any data breaches or requests from data subjects, and to assist the Client in complying with its legal obligations under data protection laws.

**11.2 Confidential Information:** Each party (the “Receiving Party”) shall keep secret and confidential all information obtained from the other party (the “Disclosing Party”) in connection with this contract that is not publicly available or is marked or identified as confidential (or that should reasonably be understood to be confidential given its nature). This includes, without limitation, source code, business plans, technical know-how, customer data, trade secrets, and any other proprietary information. The Receiving Party shall use the Disclosing Party’s Confidential Information solely for the purposes of fulfilling its obligations under this contract and shall not disclose it to any third party without the Disclosing Party’s prior written consent. The Receiving Party shall protect the confidentiality of such information with at least the same degree of care as it uses for its own similar confidential information (and no less than a reasonable standard of care). These confidentiality obligations shall continue during the term of the contract and for a period of 3 years after its termination, or indefinitely for trade secrets.

**11.3 Permitted Disclosures:** Confidential Information does not include information that (a) is or becomes public without breach of this agreement, (b) was rightfully known by the Receiving Party before disclosure, (c) is received from a third party without duty of confidentiality, or (d) is required to be disclosed by law or court order (in which case the Receiving Party shall give prompt notice to the Disclosing Party and cooperate in seeking reasonable protective measures). 

**11.4 Publicity and Portfolio Rights:** The Developer may include the Client’s name, logo, and a brief, high-level, non-confidential description of the services provided under this Agreement in the Developer’s professional portfolio, website, and promotional materials, unless the Client requests otherwise in writing.

To make the non-solicitation clause clearer, more specific, and more relaxed for the Client, we can apply three key adjustments:

1. **Narrow the Scope of Protected Personnel:** Instead of a blanket restriction on any subcontractor or collaborator of the Developer, we limit the restriction only to individuals who *actively performed work* on the Client's project within the preceding 6 months. This prevents the Client from being penalized for hiring someone who works with you but was never assigned to their project.
2. **Add a General Recruitment Exception (The "Relaxed" Element):** We can add a standard industry carve-out: if your collaborator applies to a general, public job posting by the Client without any direct targeting or solicitation, it is not considered a breach of this contract.
3. **Clarify the 10% Rate Adjustment Math:** The rate-increase formula in the original draft was slightly ambiguous. We can add a simple mathematical example to make it completely transparent and prevent future billing disputes.

## 12. Contractor Status, Subcontracting, and Non-Solicitation

**12.1 Clarification:** The Developer is an independent contractor and not an employee, agent, or partner of the Client. Nothing in this Agreement shall create any employment, joint venture, or agency relationship. 

**12.2 Non-Solicitation of Personnel:** 
The Client agrees not to directly or indirectly solicit, hire, or engage (whether as an employee, independent contractor, consultant, or otherwise) any employee, subcontractor, or collaborator of the Developer who was directly assigned to and performed work on the Client's project under this Agreement within the preceding six (6) months. This restriction applies during the term of this Agreement and for a period of six (6) months following its termination, unless the Developer provides prior written consent.

*General Recruitment Exception:* This restriction does not apply if an eligible individual responds to a general, public job advertisement, recruitment campaign, or public posting by the Client that was not specifically targeted at the personnel, employees, or subcontractors of the Developer.

*Oversight Compensation Exception:* If the Client wishes to directly engage an eligible individual and the Developer provides prior written consent, the Developer shall remain actively involved in the project as the lead or primary developer. To compensate the Developer for ongoing coordination and oversight responsibilities, the Developer’s hourly rate under this Agreement shall be increased by an amount equal to ten percent (10%) of the hourly rate paid by the Client to that newly engaged individual. 
*(For example: If the newly engaged individual is paid $50 per hour by the Client, the Developer's own hourly rate under this Agreement shall automatically increase by $5 per hour for as long as both parties remain engaged on the project).*

**12.3 Subcontracting:** The Developer may engage qualified subcontractors to perform portions of the services, provided that the Developer remains fully responsible for the performance of such subcontractors, ensures they are bound by confidentiality terms at least as restrictive as those contained herein, and remains the primary point of contact for the Client.

## 13. Payment Packages  

- One (1) of the sub-sections listed below (Sections Basic Package, Pro Package, Expert Package) must be explicitly selected and agreed upon in writing by both parties.
- In the interest of fairness, Clients of the same tier will receive equal treatment in terms of work priority.
- If the Developer fails to deliver the minimum guaranteed work hours per week, the missing time is added to the next week; however, the maximum amount of pending hours is capped at 40.  
- The Client can change the minimum guaranteed work hours at any time to something lower (also to 0 hours) by contacting the Developer.
- Guaranteed work hours are only valid while there are pending tasks to complete/deliver.

### 13.1 Basic Package  
The optimal choice for occasional developer needs when time constraints are not a factor.  

- Minimum 1 hour of work per week guaranteed, with a maximum of 4 hours.
- The Client must select the "MIT License", unless otherwise agreed in writing. 

### 13.2 Pro Package  
The best option when seeking a dependable developer for medium to large projects.  

The "Pro" rate includes some benefits over the "Basic" rate:  

- Minimum 4 hours of work per week guaranteed, with a maximum of 16 hours.
- The Client must select the "MIT License", unless otherwise agreed in writing. 
- The Client can set online live meetings, however is limited to one per week, with a maximum length of 1 hour.  
- The Clients' tasks get prioritized over Clients with the "Basic" rate.  

### 13.3 Expert Package  

The superior choice when you need a reliable and fast working, long-term Developer for larger projects.  

The "Expert" rate includes all "Pro" benefits and provides some additional benefits:  

- Minimum 8 hours of work per week guaranteed, with no maximum limit.
- The Client can get the Developers' phone number, on request and call any time.  
- The Client can benefit from online meetings, or meetings in person (if possible), with no weekly limits or hourly limits.  
- The Clients' tasks get prioritized over Clients with the "Basic" and "Pro" rates.
- The Client can set deadlines for tasks.  
  - The Developer must agree to the deadline in writing.  
  - If the Developer fails to complete the tasks by the deadline, the rate/payment for those tasks can be cut by 20%, this decision is at the sole discretion of the Client. 

## 14. Payment Logic  

- One (1) of the sub-sections listed below (Sections Prepaid, Postpaid, FPW Subscription, FP Subscription) must be explicitly selected and agreed upon in writing by both parties. Once selected, the remaining subsections shall be deemed inapplicable and without legal effect for the purposes of this Agreement. 
- For each subsection following terms also apply:
  - Payment is to be made to Developer's PayPal email osiris_support@pm.me (osiris[underScore]support[aT]pm[DoT]me), however other ways of payment are also possible but must be agreed upon in writing by both parties.
  - Payment processing fees and/or currency conversion fees are to be paid by the Developer per PayPal's "Goods and Services" payment type. 
  - The Client shall pay all amounts in full, free of any withholding tax, unless required by law (in which case the payment shall be grossed-up as necessary to ensure the Developer receives the agreed net amount). 
  - The Client has 5 days to complete the payment upon receiving the invoice email or the due date.  
  - Payment is deemed completed at the time the Developer receives confirmation by the payment processor.  
  - Any payment not made within 5 days of the due date shall accrue simple interest at the statutory rate permitted under German law for transactions between undertakings (9 percentage points above the European Central Bank base interest rate per annum), calculated on a daily basis from the due date until the date payment is received in full.
  - Upon termination, if the Client has prepaid for hours or a subscription period that has not fully elapsed, the Developer shall refund any unearned amount for work not performed, unless termination was due to the Developer's material breach (in which case a full refund of any prepayments for unused work shall be due).
  - The Developer is responsible for his own operational costs. Any extraordinary expenses (e.g., travel, special equipment or software) will only be incurred with Client's prior written approval and shall be reimbursed by the Client against receipts.

### 14.1 Prepaid (Before Work Commences)  
Ideal for clients who prefer to manage their budget closely and want to ensure that work is paid for in advance, minimizing financial risk.  

1. The Developer and Client agree on the amount of work hours to be paid.  
2. The Developer sends an invoice via email to the Client for those hours.  
3. The Client pays the invoice.  
4. The Developer works (according to the selected rate) until the paid hours are completed.  

### 14.2 Postpaid (After Work Completion)  
Suitable for clients who prefer to pay for work after it has been completed, providing them with the opportunity to review the work before making a payment. This option is only available for Clients that completed at least 500€ in Prepaid payments.  

1. The Developer and Client agree on a timespan (usually a month).  
2. The Developer works (according to the selected rate).  
3. The Developer sends an invoice via email to the Client covering the work hours of that timespan.  
4. The Client pays the invoice.  

### 14.3 FPW Subscription (Fixed Price and Work)  
Best for clients with ongoing projects who require a predictable monthly billing cycle and a consistent number of work hours.  

1. The Developer and Client agree on a timespan (usually a month) and a fixed amount of work hours for that timespan.  
2. The Developer sends an invoice via email to the Client covering that timespan.  
3. The Client pays the invoice.  
4. The Developer works (according to the selected rate).  

### 14.4 FP Subscription (Fixed Price)  
Perfect for clients who prefer a fixed monthly cost instead of paying for the complete project at once and benefit from fast project completion.  
This option is only available for Clients that completed at least 500€ in Prepaid payments.  

1. The Developer and Client agree on a timespan (usually a month) and a fixed price for that timespan and a total/maximum amount of work hours estimate (for all tasks / the complete project) that once reached, further work is paused and the Client notified.  
2. The Developer sends an invoice via email to the Client with the fixed price for that timespan.  
3. The Client pays the invoice.  
4. The Developer works (according to the selected rate) and is encouraged to exceed the work hours / the price for that timespan, which in turn prolongs the minimum runtime of the subscription to match the total costs.  

## 15. Termination Rights  

- **15.1 Termination for Convenience:** Either party may terminate this Agreement at any time, for any reason or no reason, by providing fourteen (14) calendar days' prior written notice to the other party.
- **15.2 Termination for Cause:** Either party may terminate this Agreement immediately if the other party commits a material breach of this Agreement and fails to cure such breach within seven (7) calendar days of receiving written notice describing the breach in reasonable detail.
- **15.3 Actions Upon Termination:** Upon termination:  
    - The Developer shall cease work on all pending tasks, unless otherwise agreed in writing.  
    - The Developer shall promptly deliver to the Client all completed work and any work-in-progress for which the Client has paid or is willing to pay. 
    - The Client shall remain responsible for payment of all work completed and properly invoiced prior to the effective date of termination. Payment will be made for any completed work as outlined within the Payment section.  
    - Any prepaid but unearned fees shall be refunded, and any unpaid fees for completed work shall become immediately due.  
    - The provisions related to confidentiality, intellectual property, limitations of liability, and any other terms which by their nature should survive, remain in full force and effect.  

## 16. Force Majeure

Neither party shall be liable for any delay or failure in performance of its obligations under this Agreement (except for payment obligations) resulting directly from circumstances beyond its reasonable control, including but not limited to natural disasters, acts of God, war, terrorism, riots, strikes, government mandates, pandemics, or widespread failures of public utilities or telecommunications networks. The affected party shall promptly notify the other party in writing of the Force Majeure event. Performance shall be excused for the duration of the event, provided that if the delay or failure continues for more than thirty (30) consecutive calendar days, either party may terminate this Agreement upon written notice.


```
Client Signature:  _______________________________

Client Name:       _______________________________

Date:              _______________________________



Developer Signature:  _______________________________

Developer Name:       _______________________________

Date:                 _______________________________
```
