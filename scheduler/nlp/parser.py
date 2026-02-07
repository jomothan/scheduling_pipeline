import re
from datetime import datetime, timedelta
import dateparser

class ParsedRequest:
    def __init__(self, participants, duration_minutes, start_range, end_range, time_pref):
        self.participants = participants
        self.duration_minutes = duration_minutes
        self.start_range = start_range
        self.end_range = end_range
        self.time_pref = time_pref


class NLPSchedulerParser:

    def __init__(self, current_user="jomo"):
        self.current_user = current_user.lower()

    def parse(self, text: str) -> ParsedRequest:
        text_lower = text.lower()

        participants = self._extract_participants(text_lower)
        duration = self._extract_duration(text_lower)
        start_range, end_range = self._extract_date_range(text_lower)
        time_pref = self._extract_time_preference(text_lower)

        return ParsedRequest(participants, duration, start_range, end_range, time_pref)

    def _extract_participants(self, text):
        names = re.findall(r"\b[A-Z][a-z]+\b", text)
        names = [n.lower() for n in names]

        if "me" in text:
            names.append(self.current_user)

        return list(set(names))

    def _extract_duration(self, text):
        match = re.search(r"(\d+)\s*(minutes|min)", text)
        return int(match.group(1)) if match else 30

    def _extract_date_range(self, text):
        now = datetime.now()

        if "this week" in text:
            start = now - timedelta(days=now.weekday())
            end = start + timedelta(days=6)
            return start, end

        if "tomorrow" in text:
            start = now + timedelta(days=1)
            end = start
            return start, end

        parsed = dateparser.parse(text)
        return parsed, parsed

    def _extract_time_preference(self, text):
        if "morning" in text:
            return ("09:00", "12:00")
        if "afternoon" in text:
            return ("12:00", "17:00")
        if "evening" in text:
            return ("17:00", "20:00")
        return None
