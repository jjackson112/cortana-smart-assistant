# title, description, updated time/date, etc
# usual - add, update, delete, view/show, search
# add in sort + notify reminders

from json
from datetime import datetime, timedelta

class Scheduler:
    def __init__(self, file_path="reminders.json", title, description):
        self.file_path = file_path
        self.reminders = self.load_reminders()

        self.title = title
        self.description = description

    def load_reminders(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_reminders(self):

    def greeting(self):
        print("What's on the schedule today?")

    def add_reminders(self):
        title = input("Reminder title:").strip()
        if not title:
            print("Title not found.")
            return
        
        # duplicated title

        description = input("Add a short description").strip()
        
        self.reminders.append({
            "title": title,
            "description": description,
        })

        self.save_reminders()

    def view_reminders(self):

    def search_reminders(self):

    def update_reminders(self):

    def delete_reminders(self):