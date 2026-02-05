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

    def add_task(self, task):
        task = task.strip()
        if not task:
            return "It cannot be empty."
        
        self.tasks.append(task)
        self.save_tasks()
        return "Task added"

    def show_list(self):
        if not self.tasks:
            return ["No tasks added yet."]
        
        return[f"{i+1}. {task}" for i, task in enumerate(self.tasks)]

    def update_task(self, index, updated_task):
        if not self.tasks:
            return "No tasks to update."
        
        if index < 0 or index >= len(self.tasks):
            return "Task number out of range."
        
        if not updated_task.strip():
            return "Task cannot be empty."
        
        self.tasks[index] = updated_task.strip()
        self.save_tasks()
        return "Task updated successfully."
        
    def delete_task(self, index):        
        if not self.tasks:
            return "Nothing to delete."

        if index < 0 or index >= len(self.tasks):
            return "Task number out of range."
        
        deleted = self.tasks.pop(index)
        self.save_tasks()
        return(f"Deleted: {deleted}")