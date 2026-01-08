# title, description, updated time/date, etc
# usual - add, update, delete, view/show, search
# add in sort + notify reminders

from json
from datetime import datetime, timedelta

class Scheduler:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.reminders = []

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
        
    def view_reminders():

    def search_reminders():

    def update_reminders():

    def delete_reminders():