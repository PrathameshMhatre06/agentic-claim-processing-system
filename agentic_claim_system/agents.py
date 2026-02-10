from rules import (
    classify_claim_priority,
    check_room_limit,
    check_ped
)


def intake_agent(claim):
    """
    Intake Agent:
    Receives raw claim data and passes it forward.
    """
    return claim


def policy_evaluation_agent(claim):
    """
    Policy Evaluation Agent:
    Applies insurance rules like priority, PED, and room limits.
    """
    # Priority classification
    claim["priority"] = classify_claim_priority(claim["claim_amount"])

    # PED check
    claim["ped_flag"] = check_ped(claim["ped"])

    # Room rent check (example logic)
    # Assuming room cost per day = policy_room_limit from input
    claim["room_within_limit"] = check_room_limit(
        claim["policy_room_limit"]
    )

    return claim


def decision_agent(claim):
    """
    Decision Agent:
    Decides the next action based on evaluated rules.
    """
    if claim["priority"] == "High" or claim["ped_flag"]:
        claim["decision"] = "Send for manual review"
    else:
        claim["decision"] = "Auto process"

    return claim


def summary_agent(claim):
    """
    Summary Agent:
    Generates a human-readable explanation of the decision.
    """
    claim["summary"] = (
        f"Claim of ₹{claim['claim_amount']} from {claim['hospital']} "
        f"classified as {claim['priority']} priority. "
        f"Decision: {claim['decision']}."
    )

    return claim

def investigation_agent(claim):
    if claim["priority"] == "High":
        claim["investigation_required"] = "Yes"
    else:
        claim["investigation_required"] = "No"
    return claim

def proportionate_deduction_agent(claim):
    """
    Proportionate Deduction Agent:
    Applies deduction if actual room cost exceeds policy limit.
    """
    if claim["actual_room_cost"] > claim["policy_room_limit"]:
        ratio = claim["policy_room_limit"] / claim["actual_room_cost"]
        deducted_amount = int(claim["claim_amount"] * ratio)

        claim["deduction_applied"] = "Yes"
        claim["final_payable_amount"] = deducted_amount
    else:
        claim["deduction_applied"] = "No"
        claim["final_payable_amount"] = claim["claim_amount"]

    return claim

def sub_limit_agent(claim):
    """
    Sub-Limit Agent:
    Applies treatment-specific sub-limit if applicable.
    """
    if claim["claim_amount"] > claim["treatment_sub_limit"]:
        claim["sub_limit_applied"] = "Yes"
        claim["amount_after_sub_limit"] = claim["treatment_sub_limit"]
    else:
        claim["sub_limit_applied"] = "No"
        claim["amount_after_sub_limit"] = claim["claim_amount"]

    return claim

def non_disclosure_penalty_agent(claim):
    """
    Non-Disclosure / Penalty Agent:
    Applies penalty if non-disclosure is detected.
    """
    if claim.get("non_disclosure_detected") == "Yes":
        penalty_amount = int(claim["final_payable_amount"] * 0.20)

        claim["penalty_applied"] = "Yes"
        claim["penalty_amount"] = penalty_amount
        claim["payable_after_penalty"] = (
            claim["final_payable_amount"] - penalty_amount
        )
    else:
        claim["penalty_applied"] = "No"
        claim["payable_after_penalty"] = claim["final_payable_amount"]

    return claim

def medical_image_diagnostics_agent(claim):
    """
    Simulates Medical Image Diagnostics validation
    (X-ray / MRI / CT Scan review placeholder).
    """
    if (
        claim.get("treatment_type") in ["Surgery", "Orthopedic"]
        or claim["claim_amount"] > 75000
    ):
        claim["medical_image_required"] = "Yes"
        claim["image_diagnostics_status"] = "Pending Review"
        claim["medical_risk_note"] = (
            "Medical images required for validation due to high-risk treatment."
        )
    else:
        claim["medical_image_required"] = "No"
        claim["image_diagnostics_status"] = "Not Required"
        claim["medical_risk_note"] = "No medical image diagnostics required."

    return claim
