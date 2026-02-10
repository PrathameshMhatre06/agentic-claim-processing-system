import json

from agents import (
    intake_agent,
    policy_evaluation_agent,
    medical_image_diagnostics_agent,
    investigation_agent,
    sub_limit_agent,
    proportionate_deduction_agent,
    non_disclosure_penalty_agent,
    decision_agent,
    summary_agent
)


def run_agentic_claim_flow():
    """
    Orchestrates the complete agentic workflow
    """
    with open("sample_input.json") as f:
        claim = json.load(f)

    claim = intake_agent(claim)
    claim = policy_evaluation_agent(claim)
    claim = medical_image_diagnostics_agent(claim)
    claim = investigation_agent(claim)
    claim = sub_limit_agent(claim)
    claim = proportionate_deduction_agent(claim)
    claim = non_disclosure_penalty_agent(claim)
    claim = decision_agent(claim)
    claim = summary_agent(claim)

    return claim


if __name__ == "__main__":
    final_output = run_agentic_claim_flow()
    print(json.dumps(final_output, indent=2))
