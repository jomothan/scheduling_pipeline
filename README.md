# scheduling_pipeline

### setup instructions on wsl: 
pip install dateparser pytz <br/>
cd scheduler <br/>
python3 main.py

### assumptions:
* natural language parsing is rule-based, not ai-based
* particpant names are capitalized words and "me" maps to current user
* duration is numeric minutes
* date phrases are "this week" and "tomorrow"
* time preferences are "morning", "afternoon", and "evening"
* each particpants has fixed daily wokring hours

### design decisions:
* provider interface so google api can be implemented in the future without changing logic
* ranking is separate from scheduling logic for extensible architecture
* rule-based nlp is easier to debug

### mock data details:
* inside calendars/mock_provider.py
* includes working hours and busy calendar events for each user

### wireframe
https://docs.google.com/drawings/d/1CpJdQFVuZ5bu4185koKdE1jd2gJ71mtU0_1r3z8zyz4/edit?usp=sharing