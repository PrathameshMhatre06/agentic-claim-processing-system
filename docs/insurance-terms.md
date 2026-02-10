\# Insurance Concepts Used in This Project



This document explains the key health insurance concepts

implemented and simulated in the agentic claim processing system.



---



\## PED (Pre-Existing Disease)

A medical condition that existed before the policy start date.



Impact:

\- Claims related to PED may be rejected or require detailed investigation

\- Waiting periods or exclusions may apply

\- Non-disclosure of PED can lead to penalties or claim denial



Used in Project:

\- PED flag is evaluated during policy validation

\- PED influences investigation and adjudication decisions



---



\## Room Rent Limits

Health insurance policies define a maximum allowed room rent per day.



Impact:

\- If actual room cost exceeds the policy limit,

&nbsp; proportionate deductions are applied to the total claim

\- Higher room category indirectly increases treatment cost



Used in Project:

\- Actual room cost is compared with policy room limit

\- Excess room rent triggers proportionate deduction logic



---



\## Sub-Limits

Sub-limits are caps on specific treatments or procedures

(e.g., surgery, diagnostics, maternity).



Impact:

\- Even if total sum insured is high, payouts are capped per treatment

\- Excess amount beyond sub-limit is not payable



Used in Project:

\- Treatment-wise sub-limit is applied before final settlement

\- Remaining amount flows to further evaluation stages



---



\## Adjudication

Adjudication is the final decision-making step in claim processing.



Impact:

\- Combines policy checks, investigation findings, and deductions

\- Determines final payable amount and claim status



Used in Project:

\- Decision Agent simulates adjudication outcomes

\- Generates final processing instructions



---



\## Investigation

Investigation is triggered for high-risk or high-value claims.



Impact:

\- Required for fraud detection and non-disclosure verification

\- May delay claim settlement



Used in Project:

\- High-value claims are flagged automatically

\- Investigation agent determines review requirement



---



\## Proportionate Deduction

A penalty applied when policy conditions are violated,

commonly due to room rent limits.



Impact:

\- Reduces payable amount proportionally across all expenses

\- Acts as a financial penalty for non-compliance



Used in Project:

\- Deduction logic is applied after room limit checks

\- Final payable amount reflects deductions



---



\## Summary

These insurance concepts are handled through independent agents,

making the system modular, explainable, and closer to

real-world health insurance claim workflows.



