# Agentic Claim Processing System

This project demonstrates a **pure agentic approach** to processing
health insurance claims using Python.

The system is designed using a **mono-repo structure**, where multiple
independent agents collaborate to simulate real-world insurance
claim workflows, without using any low-code or automation platforms.

---

## 🧠 Why Agentic Workflows?

Health insurance claim processing involves multiple overlapping rules,
exceptions, and validations that are difficult to scale using
traditional rule-based systems.

An **agentic approach** breaks the workflow into focused agents,
each responsible for a specific decision, making the system:

- Modular and extensible
- Easier to reason about and debug
- Closer to real insurance operations
- Ready for future AI/LLM integration

---

## 🔁 High-Level Claim Processing Flow

Claim Input  
→ Intake Agent  
→ Policy Evaluation Agent  
→ Medical Image Diagnostics Agent  
→ Investigation Agent  
→ Sub-Limit Agent  
→ Proportionate Deduction Agent  
→ Decision / Adjudication Agent  
→ Summary Agent  
→ Final Structured Output (JSON)

---

## 🤖 Agents Implemented

### Intake Agent
- Reads and validates incoming claim data

### Policy Evaluation Agent
- Evaluates core policy rules such as:
  - Claim amount thresholds
  - PED checks
  - Room rent limits

### Medical Image Diagnostics Agent
- Simulates validation of medical images (X-ray, MRI, CT scan)
- Flags when image-based review is required for high-risk treatments
- Acts as a placeholder for future ML-based diagnostics

### Investigation Agent
- Triggers investigation for high-value or risky claims
- Supports fraud detection and compliance checks

### Sub-Limit Agent
- Applies treatment-specific caps on payable amounts
- Ensures payouts adhere to policy sub-limits

### Proportionate Deduction Agent
- Applies proportional deductions when policy conditions
  such as room rent limits are violated

### Decision / Adjudication Agent
- Combines outputs from all agents
- Determines final claim handling (auto-process or manual review)

### Summary Agent
- Generates a human-readable explanation of the claim decision
- Improves transparency and explainability

---

## 🏥 Insurance Concepts Covered

- Pre-Existing Disease (PED)
- Room Rent Limits
- Sub-Limits on Treatments
- Proportionate Deduction
- Non-Disclosure and Penalties
- Insurance Investigation
- Medical Adjudication
- Medical Image Diagnostics (simulated)

(Details documented in `docs/insurance-terms.md`)

---

## 📂 Repository Structure
claim-processing-agentic/
│
├── README.md
├── docs/
│ ├── approach-comparison.md
│ └── insurance-terms.md
│
├── agentic_claim_system/
│ ├── main.py
│ ├── agents.py
│ ├── rules.py
│ └── sample_input.json

---

## 🎯 Project Objectives

- Demonstrate agentic claim processing without low-code tools
- Model real-world health insurance complexity using agents
- Provide an extensible foundation for:
  - LLM-powered decision agents
  - Medical image analytics
  - Enterprise-scale claim systems

---

## 🚀 Future Enhancements

- Integrate actual medical image analysis models
- Replace rule-based agents with LLM-driven agents
- Recreate the same workflow using an Agentic IDE
- Add fraud risk and co-pay evaluation agents

---

This project focuses on **clarity of design, domain correctness,
and extensibility**, rather than tooling complexity.