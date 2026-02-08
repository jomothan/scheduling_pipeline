# scheduling_pipeline

### setup instructions on wsl: 
pip install dateparser pytz
cd scheduler
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