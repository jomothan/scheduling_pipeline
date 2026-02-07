from datetime import timedelta

def split_into_slots(intervals, duration_minutes):
    slots = []
    duration = timedelta(minutes=duration_minutes)

    for start, end in intervals:
        current = start
        while current + duration <= end:
            slots.append((current, current + duration))
            current += timedelta(minutes=15)  # sliding window

    return slots
