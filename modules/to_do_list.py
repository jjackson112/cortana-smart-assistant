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

    def update_task(self, index):

    def delete_task(self, index):
        self.tasks.pop(index)
    
    def show_list(self):
        return self.tasks
