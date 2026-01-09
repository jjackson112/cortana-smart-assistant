# title, description, updated time/date, etc
# usual - add, update, delete, view/show, search
# add in sort + notify reminders

import json
from datetime import datetime, timedelta

class Scheduler:
    def __init__(self, file_path="events.json"):
        self.file_path = file_path
        self.events = self.load_events()

    def load_events(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_events(self):
        with open(self.file_path, "w") as file:
            json.dump(self.events, file, indent=4)

    def greeting(self):
        print("What's on the schedule today Jasmine?")

    def add_events(self):
        title = input("Event title:").strip()
        if not title:
            print("Title not found.")
            return
        
        date = None
        time = None
        schedule_type = input("Is this a meeting or a reminder?" ).strip().lower()

        if schedule_type not in ("meeting", "reminder"):
            print("Invalid type")
            return
        
        if schedule_type == "meeting":
            date = input("Enter the meeting date (MM-DD-YYYY): ").strip()
            time = input("Enter the meeting time (HH:MM): ").strip()
        else:
            reminder_date = input("Do you want to add a date? (y/n) ").lower()
            if reminder_date == "y":
                date = input("Enter the reminder date (MM-DD-YYYY): ").strip()
            
                reminder_time = input("Do you want to add a time? (y/n) ").lower()
                if reminder_time == "y":
                    time = input("Enter the reminder time (HH:MM): ").strip()

        description = input("Add a short description").strip()
        
        event ={
            "title": title,
            "type": schedule_type,
            "description": description,
            "date": date,
            "time": time,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": None
        }

        self.events.append(event)

        self.save_events()
        print("Added to calendar.")

    def list_events(self):
        if not self.events:
            print("No events added yet.")
            return
        
        print("\All events")
        for i, event in enumerate(self.events, start=1):
            print(f"{i}. {event['title']} ({event['type']})")

    def search_events(self):
        query_category = input("Would you like to look up meetings or reminders? ").strip().lower()

        if query_category not in ("meeting", "reminder"):
            print("Invalid category.")
            return
        
        found = False
        
        if query_category == "meeting":


