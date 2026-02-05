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

    def add_events(self):
        title = input("Event title: ").strip()
        if not title:
            return "Title not found."
        
        date = None
        time = None
        schedule_type = input("Is this a meeting or a reminder? ").strip().lower()

        if schedule_type not in ("meeting", "reminder"):
            return "Invalid type"

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

        description = input("Add a short description ").strip()
        
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
            return "No events added yet."
        
        self.events.sort(key=self.event_datetime)
        
        print("All events")
        for i, event in enumerate(self.events, start=1):
            print(f"{i}. {event['title']} "
                f"({event['type']}) "
                f"{event['date'] or ''} {event['time'] or ''}"
                )

    def search_events(self):
        query_category = input("Would you like to look up meetings or reminders? ").strip().lower()

        if query_category not in ("meeting", "reminder"):
            return "Invalid category."
        
        filtered_events = list(
            filter(
                lambda event: event["type"] == query_category,
                self.events
            )
        )

        if not filtered_events:
            return(f"No {query_category} found.")
        
        for event in filtered_events:
            return(f"{event['title']} ({event['date']} {event['time']})")

    def update_events(self):
        update_type = input("What needs to be updated - a meeting or a reminder? ")
        
        filtered_type = [
            event for event in self.events
            if event["type"] == update_type
        ]

        if not filtered_type:
            return "No matching event types."
        
        print(f"\n{update_type.capitalize()}s:")
        for i, event in enumerate(self.events, start=1):
            return(f"{i}. {event['title']} ({event['date']} {event['time']})")

        selection = input("Enter event number to be updated: ").strip()

        if not selection.isdigit():
            return "Invalid number"

        index = int(selection) -1

        if index < 0 or index >= len(self.events):
            return "Event number out of range."
        
        updated_event = input("Enter the updated event: ").strip()
        if not updated_event:
            return "Event cannot be empty."
    
        # Update the chosen event
        self.events[index] ["title"] = updated_event
        self.events[index]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.save_events()
        return "Event updated successfully."

    def delete_event(self):        
        if not self.events:
            return "Nothing to delete."
        
        delete_filter_type = input("Do you want to delete a meeting or a reminder? ").strip().lower()
        
        if delete_filter_type in ("meeting", "reminder"):
            filtered_events = [
                event for event in self.events
                if event["type"] == delete_filter_type
            ]
        else:
            filtered_events = self.events # show all with no filtering

        if not filtered_events:
            return "No events found to delete."
            
        print("\nEvents:")
        for i, event in enumerate(filtered_events, start=1):
            print(f"{i}. {event['title']} ({event['type']})")
        
        choice = input("Enter event number to delete. ").strip()

        if not choice.isdigit():
            return "Enter a valid number."

        index = int(choice) -1
        if index < 0 or index >= len(self.events):
            return "Event number out of range."
        
        deleted_event = filtered_events[index]
        self.events.remove(deleted_event)
        self.save_events()
        return(f"Deleted: {deleted_event['title']}")