from nlp.parser import NLPSchedulerParser
from calendars.mock_provider import MockCalendarProvider
from core.availability import invert_busy_to_free, intersect_intervals
from core.slot_generator import split_into_slots
from core.ranking import rank_slots
from datetime import datetime

def run_scheduler(request_text):
    parser = NLPSchedulerParser(current_user="jomo")
    provider = MockCalendarProvider()

    parsed = parser.parse(request_text)

    all_free_times = []

    for user in parsed.participants:
        tz = provider.get_timezone(user)
        start = parsed.start_range.astimezone(tz)
        end = parsed.end_range.astimezone(tz)

        work_start_hour, work_end_hour = provider.get_working_hours(user)
        work_start = start.replace(hour=work_start_hour, minute=0)
        work_end = start.replace(hour=work_end_hour, minute=0)

        busy = provider.get_busy_times(user, work_start, work_end)
        free = invert_busy_to_free(busy, work_start, work_end)
        all_free_times.append(free)

    common_free = intersect_intervals(all_free_times)
    slots = split_into_slots(common_free, parsed.duration_minutes)
    ranked = rank_slots(slots)

    return ranked[:5]


if __name__ == "__main__":
    request = "Find common time between me, Abdul, Samvrta, and Ralph this week for 45 minutes"
    results = run_scheduler(request)

    for start, end in results:
        print(f"{start} → {end}")
