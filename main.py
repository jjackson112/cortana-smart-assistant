# What will Cortana do as my assistant?
# She should be a program that can remember and respond

# while loop (conditionals) - command loop
# runs until condition is met - control structure
# for key, value lists everything in memory
# for loop for inside commands or methods

import json
import os

class Cortana:
    def __init__(self, name):
        self.name = name
        self.memory_path = self.get_memory_path()
        self.memory = self.load_memory()

    # Categories setup
        for category in ["personal", "work", "other"]:
            self.memory.setdefault(category, {})

    # File Handling
    def load_memory(self):
        try:
            with open(self.memory_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Memory file corrupted. Starting fresh.")
            return {}
        
    def save_memory(self):
        with open(self.memory_path, "w") as file:
            json.dump(self.memory, file, indent=4)

    def get_memory_path(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, "memory.json")
    
    # Commands
    def greeting(self):
        print(f"Hi, my name is {self.name}")

    def remember(self):
        category = input("Category (personal/work/other): ").strip().lower()

        if category not in self.memory:
            print("Unknown category, using 'other'.")
            category = "other"

        key = input("What should I remember? ").strip()
        if not key:
            print("Key cannot be empty!")
            return
            
        value = input(f"What is '{key}'? ").strip()
        if not value:
            print("Value cannot be empty!")
            return
            
        self.memory[category][key] = value
        self.save_memory()
        print(f"Got it! I'll remember '{key}' in {category}.")

            
    def list_memory(self):
        has_memory = False
        for category, items in self.memory.items():
            if items:
                print(f"\n[{category.capitalize()}]")
                for key, value in items.items():
                    print(f"{key}: {value}")
                has_memory = True

        if not has_memory:
            print("I don't remember anything yet.")

        if not self.memory:
            print("I don't remember this.")
        else:
            for key, value in self.memory.items():
                print(f"{key}: {value}")

    def search(self):
        query = input("What do you wnat to search for? ").strip().lower()
        if not query:
            print("Search query cannot be empty.")
            return
        
        found = False
        for category, items in self.memory.items():
            results = {k:v for k,v in items.items() if query in k.lower()}
            if results:
                print(f"\n[{category.capitalize()}]")
                for k, v in results.items():
                    print(f"{k}: {v}")
                found = True

        if not found:
            print("There are no matching memories.")

    # where to update, verify category exists, ask what to update, ask for new value and save
    # self.memory[category][key] = new_value
    def update(self):
        category = input("What category needs to be updated? ").strip().lower()

        if category not in self.memory:
            print("Category does not exist.")
            return

        key = input("What should I update? ").strip()
        if not key:
            print("Key cannot be empty.")
            return
        
        if key not in self.memory[category]:
            print("That does not exist.")
            return

        updated_value = input(f"What should '{key}' be updated to? ").strip()
        if not updated_value:
            print("Value cannot be empty.")
            return

        self.memory[category][key] = updated_value
        self.save_memory()
        print(f"Updated '{key}' in {category}.")
        
# Main program loop
if __name__ == "__main__":
    cortana = Cortana("Cortana")
    cortana.greeting()

    while True:
        command = input("\nEnter a command (remember, list, search, exit):").strip().lower()
        
        if command == "exit":
            print("Bye!")
            break

        elif command == "remember":
            cortana.remember()
            
        elif command == "list":
            cortana.list_memory()

        elif command == "search":
            cortana.search()
        else:
            print("I don't understand that command.")    
