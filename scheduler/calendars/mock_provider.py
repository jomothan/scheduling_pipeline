from datetime import datetime, time
import pytz

class MockCalendarProvider:

    def __init__(self):
        self.timezones = {
            "jomo": "America/New_York",
            "abdul": "Europe/London",
            "samvrta": "Asia/Kolkata",
            "ralph": "America/Los_Angeles"
        }

        self.working_hours = {
            "jomo": (9, 17),
            "abdul": (8, 16),
            "samvrta": (10, 18),
            "ralph": (9, 17)
        }

        self.busy_data = {
            "jomo": [(time(10, 0), time(11, 0))],
            "abdul": [(time(13, 0), time(14, 0))],
            "samvrta": [(time(15, 0), time(16, 0))],
            "ralph": [(time(11, 30), time(12, 30))]
        }

    def get_timezone(self, user):
        return pytz.timezone(self.timezones[user])

    def get_working_hours(self, user):
        return self.working_hours[user]

    def get_busy_times(self, user, start_dt, end_dt):
        busy = []
        for start_t, end_t in self.busy_data.get(user, []):
            busy.append((
                start_dt.replace(hour=start_t.hour, minute=start_t.minute),
                start_dt.replace(hour=end_t.hour, minute=end_t.minute)
            ))
        return busy
