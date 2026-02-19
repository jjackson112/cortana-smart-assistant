# title, description, updated time/date, etc
# usual - add, update, delete, view/show, search
# add in sort + notify reminders

import json
from datetime import datetime
from pathlib import Path

class Scheduler:
    def __init__(self, file_path="data/events.json"):
        self.file_path = Path(file_path)
        self.events = self.load_events()

    def load_events(self):
        if not self.file_path.exists():
            return []
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_events(self):
        with open(self.file_path, "w") as file:
            json.dump(self.events, file, indent=4)

    def add_events(self, title, event_type, description="", date=None, time=None):
        if not title:
            return "Title not found."

        event_type = event_type.strip().lower()
        if event_type not in ("meeting", "reminder"):
            return "Invalid type"

        event ={
            "title": title.strip(),
            "type": event_type,
            "description": description.strip(),
            "date": date,
            "time": time,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": None
        }

        self.events.append(event)
        self.save_events()
        return "Added to calendar."

    def event_datetime(self, event):
        if not event ["date"]:
            return datetime.max # pushes undated reminders to the end
        
        date_str = event["date"]
        time_str = event["time"] or "00:00"

        return datetime.strptime(
            f"{date_str} {time_str}",
            "%m-%d-%Y %H:%M"
        )

        # self.events.sort(key=self.event_datetime) - events in chronological order

    def list_events(self):
        if not self.events:
            return []
        
        return sorted(self.events, key=self.event_datetime)
        
    def search_events(self, event_type):
        event_type = event_type.lower()
        if event_type not in ("meeting", "reminder"):
            return []
        
        return [
            event for event in self.events
            if event["type"] == event_type
        ]

    def update_events(self, index, field, updated_value):
        if index < 0 or index >= len(self.events):
            return "Invalid event index."

        if not updated_value.strip():
            return "Value cannot be empty."

        event = self.events[index]

        if field not in ("title", "description", "date", "time"):
            return "Invalid field."

        event[field] = updated_value.strip()
        event["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.save_events()
        return "Event updated successfully."

    def delete_event(self, index):        
        if not self.events:
            return "No event found"
        
        if index < 0 or index >= len(self.events):
            return "Invalid event."
        
        deleted_event = self.events[index]
        self.events.remove(deleted_event)
        self.save_events()
        return f"Deleted: {deleted_event['title']}"