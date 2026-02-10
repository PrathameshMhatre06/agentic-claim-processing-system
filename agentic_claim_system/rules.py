# Insurance policy rules

# Room rent limit per day (example policy rule)
ROOM_LIMIT_PER_DAY = 8000


def check_room_limit(room_cost_per_day):
    """
    Checks whether the claimed room cost is within policy limits.
    """
    if room_cost_per_day <= ROOM_LIMIT_PER_DAY:
        return True
    return False


def classify_claim_priority(claim_amount):
    """
    Classifies claim priority based on claim amount.
    """
    if claim_amount > 80000:
        return "High"
    return "Normal"


def check_ped(ped_status):
    """
    Checks if Pre-Existing Disease (PED) is present.
    """
    if ped_status.lower() == "yes":
        return True
    return False
