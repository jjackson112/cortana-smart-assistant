import json

class ToDo:
    def __init__(self, tasks):
        self.tasks = []

    def greeting(self):
        print("What's on your to do list? ")

    def add_task(self, task_name):
        self.tasks.append({
            "title": task_name,
            "completed": False
        })

    def update_task(self):

    def delete_task(self):
    
    def show_list(self):
        return self.tasks
