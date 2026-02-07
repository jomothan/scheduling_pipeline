from datetime import datetime, timedelta

def invert_busy_to_free(busy_slots, work_start, work_end):
    free = []
    current = work_start

    for b_start, b_end in sorted(busy_slots):
        if current < b_start:
            free.append((current, b_start))
        current = max(current, b_end)

    if current < work_end:
        free.append((current, work_end))

    return free


def intersect_intervals(list_of_interval_lists):
    result = list_of_interval_lists[0]

    for intervals in list_of_interval_lists[1:]:
        new_result = []
        for a_start, a_end in result:
            for b_start, b_end in intervals:
                start = max(a_start, b_start)
                end = min(a_end, b_end)
                if start < end:
                    new_result.append((start, end))
        result = new_result

    return result
