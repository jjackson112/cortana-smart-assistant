# If code prints data → helper method
# If code changes data → action method
# If code does both → refactor
import json
from pathlib import Path

class ToDo:
    def __init__(self, file_path="data/todos.json"):
        self.file_path = Path(file_path)
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not self.file_path.exists():
            return []
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except:
            (FileNotFoundError, json.JSONDecodeError)
            return []

    def save_tasks(self):
        with open(self.file_path, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        task = input("Add a new task: ").strip()
        if not task:
            return "It cannot be empty."
        
        self.tasks.append(task)
        self.save_tasks()
        return "Task added"

    def show_list(self):
        if not self.tasks:
            return ["No tasks added yet."]
        
        return[f"{i+1}. {task}" for i, task in enumerate(self.tasks)]

    def update_task(self):
        if not self.tasks:
            print("No tasks to update.")
            return

        self.show_list() # enumerate lives here now
        select = input("Enter the task number to update: ").strip()

        if not select.isdigit():
            print("Enter a valid number.")
            return
        
        index = int(select) -1
        if index < 0 or index >= len(self.tasks):
            print("Task number out of range.")
            return
        
        updated_task = input("Enter the updated task: ").strip()
        if not updated_task:
            print("Task cannot be empty.")
            return
        
        self.save_tasks()
        self.tasks[index] = updated_task
        print("Task updated successfully.")
        
    def delete_task(self):        
        if not self.tasks:
            print("Nothing to delete.")
            return
        
        self.show_list()
        choice = input("Enter task number to delete: ").strip()

        if not choice.isdigit():
            print("Enter a valid number.")
            return

        index = int(choice) -1
        if index < 0 or index >= len(self.tasks):
            print("Task number out of range.")
            return
        
        self.save_tasks()
        deleted = self.tasks.pop(index)
        print(f"Deleted: {deleted}")