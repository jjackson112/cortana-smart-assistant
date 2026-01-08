from json
from datetime import datetime, timedelta

class Scheduler:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.reminders = []