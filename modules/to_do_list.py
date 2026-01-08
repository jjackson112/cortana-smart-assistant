import json

class ToDo:
    def __init__(self, tasks):
        self.tasks = []

    def greeting(self):
        print("What's on your to do list? ")

    def add_task(self):
        task = input("Add a new task: ").strip()
        if not task:
            print("It cannot be empty.")
            return
        self.tasks.append(task)
        print("Task added")

    def update_task(self):
        if not self.tasks:
            print("No tasks to update.")
            return

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def delete_task(self, index):
        self.tasks.pop(index)
        
        if not self.tasks:
            print("Nothing to delete.")
            return
        
        self.show_tasks()

        choice = input("Enter task number to delete.")

        try:
            index = int(choice) -1
        
        except ValueError:
            print("Invalid number.")
            return

        if index < 0 or index >= len(self.tasks):
            print("Task number out of range.")
            return
        
        deleted = self.tasks.pop(index)
        print(f"Deleted: {deleted}")
    
    def show_list(self):
        return self.tasks

        if not self.tasks:
            print("No tasks added yet.")
            return
        
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")