from abc import ABC, abstractmethod

class CalendarProvider(ABC):

    @abstractmethod
    def get_busy_times(self, user, start_dt, end_dt):
        """Return list of (start, end) busy intervals"""
        pass

    @abstractmethod
    def get_working_hours(self, user):
        """Return (start_hour, end_hour) in local time"""
        pass

    @abstractmethod
    def get_timezone(self, user):
        pass
