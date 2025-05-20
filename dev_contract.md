#  Contract for development on software projects

- A list of changes can be found [here](https://github.com/Osiris-Team/Osiris-Team/commits/main/dev_contract.md).
- This file can be viewed as a raw text file [here](https://raw.githubusercontent.com/Osiris-Team/Osiris-Team/main/dev_contract.md).
- This contract can be transformed into a .pdf [here](https://md2pdf.netlify.app/) or into .docx/.odt (word document) [here](https://www.vertopal.com/en/convert/md-to-odt).

## Applicable parties

| Identifier  | Full Name | Address | Github ID |
| ----------- | ----------- |----------- | ----------- |
| The Client / Client | _INSERT_ | _INSERT_ | _INSERT_ |
| The Developer / Developer | Arman Ruben Kandel | Taunusstraße 124, 41236 Mönchengladbach, Germany | Osiris-Team |

## Variables

### Selected payment rate: _INSERT_ (Basic, Pro or Expert)
### Selected payment logic: _INSERT_ (Prepaid, Postpaid, FPW Subscription or FP Subscription)
### Selected copyright terms: _INSERT_ (MIT License, Custom License, Copyright transfer)


## Validity

- All parties have freely agreed to the following and look forward to working together.
- Any previous versions are superseded upon mutual acceptance and transmission of a dated signed copy.
- This contract intended to be valid from acceptance by all parties until termination.
- Either party may terminate this Agreement at any time, provided that written notice is given to the other party.
- If terminated prior to the specified deadline, payment will be made for any completed work as outlined within the [Payment](#Payment) section.

## Governing Law

This Agreement shall be governed by and construed in accordance with the laws of Germany. Any disputes arising under this Agreement shall be subject to the exclusive jurisdiction of the courts located in Mönchengladbach, Germany.

## Good faith and notice

- The Developer will act in good faith (i.e will not attempt deception or defraud
via methods including but not limited to double billing of hours or making “changes for changes sake” i.e ).
- Any potential breach of good faith, will lead to a discussion before
exploring other options.

## Scope of Work

Task List: The Developer will receive a list of tasks consisting of, for example, feature requests or bug fixes.

Task Clarity: These tasks must be clear and concise. The Client must respond to the Developer’s questions if anything is unclear.

Task Rejection: The Developer may reject one or more tasks but must provide a clear and concise reason. If the Developer rejects a task after starting work, the associated time must not be billed.

Task Priority: The Developer retains the sole discretion to determine the order, priority, and selection of tasks to be undertaken and delivered, provided such decisions do not conflict with any agreed-upon deadlines or priority arrangements. 

Delivery: All completed tasks must be delivered by the Developer in one of the following ways, depending on who owns or maintains the repository:

  1. When the Client or a Third-Party created or owns the repository:
     - The Developer must submit the task as a separate Merge Request (MR) to the Client’s upstream repository (or fork), using a descriptive branch name and meaningful commit messages.
     - For simplicity the Developer might also ask for permission to instead create a single MR containing multiple tasks.
     - Alternatively, if the Client uses an upstream public repository owned by another party, the Developer may submit a separate MR to the upstream repository, with the Client copied or tagged.

  2. When the Developer created or owns the repository:
     - The Developer may push changes as a commit to their own repository.
     - The Client is responsible for creating a fork, cloning the repository, or exporting the work to integrate it into their environment.

Delivery Frequency: The amount and frequency of deliveries is at the sole discretion of the Developer.

Delivery Labeling: All deliveries must be clearly labeled and must reference the original tasks or issues they are intended to fulfill. The Client is responsible for testing whether the delivery fulfills the task requirements. 

Delivery Notification: The Client must be notified about a delivery in writing or via electronic communication and include a link to the MR or commit.

Delivery Usage and Testing: The Client assumes all responsibility for use, deployment, and integration of the delivery in production systems, including proper testing, security, and compliance. The Client is responsible for testing whether the delivery fulfills the task requirements.

Delivery Rejection: The Client may reject or request revisions for a task but must provide written, actionable feedback. Its important to distinguish between a revision and refund requests, because the resulting additional work for the Developer is billed normally in the case of revisions. Refund requests are discussed further below.

Delivery Acceptance: A delivery is considered acceptable and billable if the Client provides written approval, or ninety (90) calendar days pass after delivery without written rejection.

90-Day Review Period: The Client has up to ninety (90) calendar days from delivery of a task to:
  - Review and test the submitted work,
  - Provide written feedback or revision requests, or
  - Notify the Developer of material defects.

90-Day Functionality Warranty and Refund Period: The Developer warrants that the delivery will operate in accordance with the agreed-upon specifications and requirements for a period of ninety (90) calendar days following the delivery date. If the Client determines that the delivery exhibits defects, errors, or fails to meet the specified requirements within this timeframe, the Client may request a refund for any task of the delivery. The Developer shall, at their own expense and within a reasonable timeframe, correct or replace the non-conforming software to ensure compliance with the agreed-upon specifications, or istead provide the refund. Exclusions: The warranty does not cover issues arising from and a refund is not possible when:
- Modifications or alterations were made to the delivery by anyone other than the Developer.
- The affected parts of the delivery have been materially modified.
- The Client performed misuse, negligence, or unauthorized use of the delivery.
- Environmental factors or hardware malfunctions that are not under the Developer's control.

Exclusive Remedy: The remedies provided in this section are the Client's sole and exclusive remedies for any breach of the warranty.

Refund Amount: The refund amount shall be calculated based on, and limited to, the number of hours directly attributable to the affected task at the time of delivery, multiplied by the applicable rate in effect at that time.

Refund Finality: Once a refund is issued, the Developer has no further obligations for the refunded task, and the Client waives future claims related to that task.

Dispute Resolution: Both parties agree to first attempt resolution via good faith negotiation before escalating to mediation, arbitration, or legal action. 

## Timing

- Time not spent actively working on a task
(e.g. Research or writing / committing code), is the Developer' to use as they see fit.
- The Developer can multitask at their complete discretion.
- There is no fixed hours to encourage a healthy study/life/work balance.

## License and Copyright

This section outlines multiple licensing models and copyright arrangements applicable to the Work Product delivered under this Agreement.

Selection Requirement: One (1) of the sub-sections listed below (Sections MIT License, Custom License, Copyright tranfer) must be explicitly selected and agreed upon in writing by both parties. Once selected, the remaining subsections shall be deemed inapplicable and without legal effect for the purposes of this Agreement.

Each sub-section governs the Client’s and Developer’s rights, obligations, and limitations regarding use, modification, and ownership of the Work Product. The selected model shall override any conflicting provisions elsewhere in this Agreement, except where otherwise explicitly stated.

### MIT License

Copyright 2025 Arman Ruben Kandel (Osiris-Team)

Permission is hereby granted to the Client obtaining a copy of the Developers' commits/changes, software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

### Custom License

Copyright 2025 Arman Ruben Kandel (Osiris-Team)

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

All software, code, documentation, designs, and other materials created under this Agreement (collectively, the "Work Product") will remain the intellectual property of the Developer.

Upon full payment and acceptance of a task, the Client is granted an exclusive, perpetual, worldwide, royalty-free license to use, modify, reproduce, display, distribute, and create derivative works of the Work Product at the state it existed upon completion/delivery of the task, for any purpose, including commercial use.
 
The Developer shall not reproduce, license, or distribute the Work Product, or any substantially similar derivative, to any third party. The Client has full practical control of the Work Product as if it were their own, except for claiming original authorship or asserting copyright ownership.

### Copyright transfer

Transfer of Ownership: Upon full payment and acceptance of the project, the Developer agrees to transfer all rights, title, and interest, including copyright, for all software, code, documentation, designs, and other materials created under this Agreement (collectively, the Work Product) to the Client. The Developer agrees that the Work Product is the exclusive property of the Client. This leads to the Client having the exclusive, perpetual, worldwide, royalty-free right to use, modify, reproduce, display, distribute, and create derivative works of the Work Product for any purpose, including commercial use.

Developer License: To facilitate continued development, the Client grants the Developer a temporary, non-exclusive, non-transferable license to use, modify, and access the Work Product.
This license is valid only while this contract remains active and un-terminated.
The license exists solely for the purpose of completing ongoing or future Deliveries under this Agreement.
Upon termination of this contract for any reason, this license is immediately revoked, and the Developer agrees to cease all use of the Work Product unless otherwise agreed in writing.

Developer Restrictions: The Developer agrees not to reproduce, license, or distribute the Work Product, or any substantially similar derivative, to any third party.

Use of Third Party and Open-Source Software: The Developer may use third-party and/or open-source software components as part of the deliverables. The Developer shall: 
- Disclose all open-source software libraires used.
- Ensure that all third-party components comply with licenses that allow commercial use, modification and redistribution.

## Background Technology

Developer Ownership: Any pre-existing tools, components, or libraries developed by the Developer prior to or outside the scope of this agreement remain the property of the Developer.

Client License: The Developer grants the Client a non-exclusive, perpetual, worldwide, and royalty-free license to use, modify, and distribute any Developer-owned Background Technology incorporated into the Work Product, solely as necessary for the use and operation of the Work Product as delivered.

This license does not apply to any Background Technology or component that is governed by an existing license (including third-party open-source software), which shall apply in accordance with its own terms. The Developer represents and warrants that all such components will be clearly disclosed and properly attributed at the time of delivery.

Developer Use: The Developer retains the right to use Background Technology for other projects, provided it does not infringe upon the Client's rights in the Work Product developed.

Survival of Terms: The provisions of this section shall survive the termination or expiration of this Agreement.

## Limitations of Liability

Except as expressly provided in the "Scope of Work" and "License and Copyright" sections of this Agreement, all software, source code, documentation, and other deliverables (collectively, the “Work Product”) are provided “AS IS”, without any warranties of any kind—whether express, implied, statutory, or otherwise. This includes, but is not limited to, implied warranties of merchantability, fitness for a particular purpose, non-infringement, or warranties arising from a course of dealing, usage, or trade practice.

To the fullest extent permitted under applicable law:

- The Developer shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including, but not limited to, loss of profits, loss of data, business interruption, or loss of business opportunities, even if the Developer has been advised of the possibility of such damages.
- The Developer’s total cumulative liability under this Agreement shall not exceed the total fees actually paid by the Client for the specific task or deliverable giving rise to the claim.
- The Developer’s liability for any breach of warranty is strictly limited to the correction or replacement of the non-conforming Work Product, as outlined in the "Scope of Work" section.

Third-party or open-source components incorporated into the Work Product are subject to their respective licenses, which may include “AS IS” disclaimers. The Client acknowledges and accepts the terms of such licenses and understands that the Developer does not provide any additional warranties for third-party or open-source software beyond compliance with license terms and proper attribution.

Nothing in this section shall exclude or limit liability for gross negligence, fraud, or willful misconduct, where such exclusion or limitation is not permitted by applicable law.


## Data Protection

If the Work Product or services involve processing of personal data, the Developer agrees to comply with all applicable data protection laws, including the EU General Data Protection Regulation (GDPR), to the extent applicable. Client remains the Data Controller; Developer acts as Data Processor.

## Independent Contractor

The Developer is an independent contractor and not an employee, agent, or partner of the Client. Nothing in this Agreement shall create any employment, joint venture, or agency relationship.

## Payment rates

In the interest of fairness;
- Clients of the same tier will recive equal treatement in terms of work priority.

### Basic rate
#### 20€ per hour

The optimal choice for occasional developer needs when time constraints are not a factor.

- Minimum 1 hour of work per week guaranteed.

### Pro rate
#### 40€ per hour

The best option when seeking a dependable developer for medium to large projects.

The "Pro" rate includes some benefits over the "Basic" rate:

- Minimum 4 hours of work per week guaranteed.
- The Client can set online live meetings or meetings in person if possible.
- The Client can set deadlines for tasks.
  - The Developer must agree to the deadline in writing.
  - If the Developer fails to complete the tasks by the deadline, the rate/payment for those tasks can be cut by 50%, this decision is at the sole discretion of the Client.
- The Clients' tasks get prioritized over Clients with the "Basic" rate.

### Expert rate
#### 80€ per hour

The superior choice when you need a reliable and fast working, long-term Developer for larger projects.

The "Expert" rate includes all "Pro" benefits and provides some additional benefits:

- Minimum 8 hours of work per week guaranteed.
- The Client can get the Developers' phone number, on request and call any time.
- The Client can benefit from live-chat and screen-sharing support.
- The Clients' tasks get prioritized over Clients with the "Basic" and "Pro" rates.

### Details

- If the Developer fails to deliver the minimum guaranteed work hours per week, the missing time is added to the next week, however the maximum amount of pending hours is capped at 40.
- The Client can change the minimum guaranteed work hours at any time to something lower (also to 0 hours) by contacting the Developer.
- The rate used in the payment will be the rate with the latest proposal date and mentioned at the top of the contract.
- Payment is to be made to Developer's PayPal email osiris_support@pm.me (osiris[underScore]support[aT]pm[DoT]me).
- Payment processing fees and/or currency conversion fees are to be paid by the Developer per PayPal's "Goods and Services" payment type.

## Payment logic

There are different ways to handle payments (listed below), for different kinds of customers.
For each payment logic following terms also apply:
- The Client has 5 days to complete the payment upon receiving the invoice email or the due date.
    - Payment is deemed completed at the time the Developer receives
      confirmation by the payment processor.
- If payment is not received 24 hours after the above time frame, a 15% lateness fee can be added to the overall balance per week.
<br>For example:

| Date                                   | Amount Due  |
| -------------------------------------- | ---- |
| July 2023 Invoice | 30.00 |
| August 3rd | 34.5 |
| August 7th | 39.67 |
| August 14th | 45.62 |
| August 21st | 52.47 |
| August 28th | 60.34 |

### Prepaid (Before Work Commences)
Ideal for clients who prefer to manage their budget closely and want to ensure that work is paid for in advance, minimizing financial risk.

1. The Developer and Client agree on the amount of work hours to be paid.
2. The Developer sends an invoice via email to the Client for those hours.
3. The Client pays the invoice.
4. The Developer works (according to the selected rate) until the paid hours are completed. 

### Postpaid (After Work Completion)
Suitable for clients who prefer to pay for work after it has been completed, providing them with the opportunity to review the work before making a payment. This option is only available for Clients that completed at least 500€ in Prepaid payments.

1. The Developer and Client agree on a timespan (usually a month).
2. The Developer works (according to the selected rate). 
3. The Developer sends an invoice via email to the Client covering the work hours of that timespan.
4. The Client pays the invoice.

### FPW Subscription (Fixed Price and Work)
Best for clients with ongoing projects who require a predictable monthly billing cycle and a consistent number of work hours.

1. The Developer and Client agree on a timespan (usually a month) and a fixed amount of work hours for that timespan.
2. The Developer sends an invoice via email to the Client covering that timespan.
3. The Client pays the invoice.
4. The Developer works (according to the selected rate). 

### FP Subscription (Fixed Price)
Perfect for clients who prefer a fixed monthly cost instead of paying for the complete project at once
and benefit from fast project completion.
This option is only available for Clients that completed at least 500€ in Prepaid payments.

1. The Developer and Client agree on a timespan (usually a month) and a fixed price for that timespan
and a total/maximum amount of work hours estimate (for all tasks / the complete project) that once reached, further work is paused and the Client notified.
2. The Developer sends an invoice via email to the Client with the fixed price for that timespan.
3. The Client pays the invoice.
4. The Developer works (according to the selected rate) and is encouraged to exceed the work hours / the price for that timespan,
which in turn prolongs the minimum runtime of the subscription to match the total costs.  


