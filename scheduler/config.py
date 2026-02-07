import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    # General
    APP_NAME: str = "SmartScheduler"
    DEFAULT_SLOT_STEP_MINUTES: int = 15
    DEFAULT_MEETING_DURATION: int = 30

    # Calendar Provider चयन
    CALENDAR_PROVIDER: str = os.getenv("CALENDAR_PROVIDER", "mock")  # "mock" or "google"

    # Timezone handling
    DEFAULT_TIMEZONE: str = "UTC"

    # Ranking preferences
    PREFER_EARLIEST: bool = True
    AVOID_LUNCH_HOURS: bool = True
    LUNCH_WINDOW: tuple = (12, 13)  # 12:00–13:00 local time

    # Google API (used only if provider == "google")
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET", "")
    GOOGLE_REDIRECT_URI: str = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/oauth2callback")

    # Service behavior
    MAX_RESULTS: int = 5


# Singleton-style config object
config = AppConfig()
