#  Contract for development on software projects

- A list of changes can be found [here](https://github.com/Osiris-Team/Osiris-Team/commits/main/dev_contract.md).
- This file can be viewed as a raw text file [here](https://raw.githubusercontent.com/Osiris-Team/Osiris-Team/main/dev_contract.md).
- This contract can be transformed into a .pdf [here](https://md2pdf.netlify.app/) or into .docx/.odt (word document) [here](https://www.vertopal.com/en/convert/md-to-odt).

## Applicable parties

| Identifier  | Full Name | Address | Github ID |
| ----------- | ----------- |----------- | ----------- |
| The Client / Client | ENTER | ENTER | ENTER |
| The Developer / Developer | Arman Ruben Kandel | Taunusstraße 124, 41236 Mönchengladbach, Germany | Osiris-Team |

### Selected payment rate: INSERT (Basic, Pro or Expert)
### Selected payment logic: INSERT (Prepaid, Postpaid, FPW Subscription or FP Subscription)

```



```
Client, signed DATE.

```



```
Developer, signed DATE.

## Validity

- All parties have freely agreed to the following and look forward to working together.
- Any previous versions are superseded upon mutual acceptance and transmission of a dated signed copy.
- Termination is possible anytime, by all parties.
- This contract intended to be valid from acceptance by all parties until termination.
- If terminated prior to the specified deadline, payment will be made for any completed work
as outlined within the [Payment](#Payment) section.

## Good faith and notice

- The Developer will act in good faith (i.e will not attempt deception or defraud
via methods including but not limited to double billing of hours or making “changes for changes sake” i.e ).
- Any potential breach of good faith, will lead to a discussion before
exploring other options.

## Scope of Work

- The Developer will receive a list of tasks consisting of, for example, feature requests or bug fixes.
- These tasks must be clear and concise. The Client must respond to the Developer’s questions if anything is unclear.
- The Developer may reject one or more tasks but must provide a clear and concise reason.
    - If the Developer rejects a task **after starting work**, the associated time **must not** be billed.
- Each **completed task** must be submitted by the Developer in one of the following ways, depending on who owns or maintains the repository:

  1. When the Client or a Third-Party created or owns the repository:
     - The Developer must submit the task as a separate Merge Request (MR) to the Client’s upstream repository (or fork), using a descriptive branch name and meaningful commit messages.
     - Alternatively, if the Client uses an upstream public repository owned by another party, the Developer may submit a separate MR to the upstream repository, with the Client copied or tagged.

  2. When the Developer created or owns the repository:
     - The Developer may push changes as a commit to their own repository.
     - In this case, the Developer must notify the Client and provide the relevant commit hash or branch name on request.
     - The Client is responsible for creating a fork, cloning the repository, or exporting the work to integrate it into their environment.

- All submissions must be clearly labeled and must reference the original task or issue they are intended to fulfill.
- The Client is responsible for testing whether the submission fulfills the task requirements.
- The Client may reject or request revisions for a task but must provide written, actionable feedback.
- A task is considered **accepted and billable** if:
    - (a) The Client provides written approval, or  
    - (b) Ninety (90) calendar days pass after delivery without written rejection.

## Quality Guarantee and Refund Policy

- 90-Day Review Period: The Client has up to ninety (90) calendar days from delivery of a task to:
  - Review and test the submitted work,
  - Provide written feedback or revision requests, or
  - Notify the Developer of material defects.

- Refund Eligibility: The Client may request a **partial refund** for any task if:
    - The work materially fails to meet agreed specifications, and
    - The issue is reported within the 90-day review window, and
    - The task has not been materially modified or integrated into production systems.
- Developer's Opportunity to Remedy: Before a refund is issued, the Developer has at least **fourteen (14) calendar days** to correct or replace the defective work.
- Scope of Refunds:  
  - The refund amount shall be calculated based on, and limited to, the number of hours directly attributable to the affected task at the time of delivery, multiplied by the applicable rate in effect at that time.
  - No refunds will be issued for tasks approved, deployed, or altered after delivery unless the defect clearly predates such actions.
  - Refunds are not available after the **90-day review window** has expired.
- Finality: Once a refund is issued, the Developer has no further obligations for the refunded task, and the Client waives future claims related to that task.
- Dispute Resolution: Both parties agree to first attempt resolution via good faith negotiation before escalating to mediation, arbitration, or legal action.

## Timing

- Time not spent actively working on a Merge Request (MR)
(e.g. Research or writing / committing code), is the Developer' to use as they see fit.
- The Developer can multitask at their complete discretion.
- There is no fixed hours to encourage a healthy study/life/work balance.
- Time tracking can be done via a comment within each MR after the applicable lines of code
have been pushed such as the following example (using ISO-8601 and 24hr clock):
    - 2023-05-16
    - 08:00 - 10:20
    - 12:00 - 13:15
    - Which would be processed as 3h 35m via the following formula: (HR * 3) + (HR * 0.35).

## License and Copyright

Copyright 2023 Arman Ruben Kandel (Osiris-Team)

Permission is hereby granted to the Client obtaining a copy of the Developers' commits/changes, software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Payment rates

In the interest of fairness;
- Clients of the same tier will recive equal treatement in terms of work priority.
- When / If a / additional higher rate client(s) is / are taken on board, "Basic" rate clients are to be advised e.g. 
  "Due to a recent increase in the number of higher tier rated clients (who's tasks have priority), I may take some additional time to respond. My appologies."

### Basic rate
#### 20€ per hour

The optimal choice for occasional developer needs when time constraints are not a factor.

- Minimum 1 hour of work per week guaranteed.

### Pro rate
#### 40€ per hour

The best option when seeking a dependable developer for medium to large projects.

The "Pro" rate includes some benefits over the "Basic" rate:

- Minimum 4 hours of work per week guaranteed.
- The Client can set deadlines for tasks.
  - The Developer must agree to the deadline in writing and can disagree within 3 days, otherwise, the Developer agrees automatically.
  - If the Developer fails to complete the tasks by the deadline, the rate/payment for those tasks is cut by 50%.
- The Clients' tasks get prioritized over Clients with the "Basic" rate.

### Expert rate
#### 80€ per hour

The superior choice when you need a reliable and fast working, long-term Developer for larger projects.

The "Expert" rate includes all "Pro" benefits and provides some additional benefits:

- Minimum 8 hours of work per week guaranteed.
- The Client can set online live meetings or meetings in person if possible.
- The Client can get the Developers' phone number, on request and call any time.
- The Client can benefit from live-chat and screen-sharing support.
- The Clients' tasks get prioritized over Clients with the "Basic" and "Pro" rates.

### Details

- If the Developer fails to deliver the minimum guaranteed work hours per week, the missing time is added to the next week.
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


