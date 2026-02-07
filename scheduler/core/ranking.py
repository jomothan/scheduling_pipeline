def rank_slots(slots):
    # Simple strategy: earliest first
    return sorted(slots, key=lambda s: s[0])
