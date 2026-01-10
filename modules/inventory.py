# What will Cortana do as my assistant?
# She should be a program that can remember and respond

# while loop (conditionals) - command loop
# runs until condition is met - control structure
# for key, value lists everything in memory
# for loop for inside commands or methods

import json
import os
from datetime import datetime

class Inventory:
    def __init__(self):
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
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    def save_memory(self):
        with open(self.memory_path, "w") as file:
            json.dump(self.memory, file, indent=4)

    def get_memory_path(self):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory.json")
    
    # Commands
    def remember(self):
        category = input("Category (personal/work/other): ").strip().lower()

        if category not in self.memory:
            print("Unknown category, using 'other'.")
            category = "other"

        key = input("What key should I remember? ").strip()
        if not key:
            print("Key cannot be empty!")
            return
            
        value = input(f"What is the value of '{key}'? ").strip()
        if not value:
            print("Value cannot be empty!")
            return
        
        # Timestamp added
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.memory[category][key] = {"value": value, "timestamp": timestamp}

        self.save_memory()
        print(f"Got it! I'll remember '{key}' in {category}.")

            
    def list_memory(self):
        has_memory = False
        for category, items in self.memory.items():
            if items:
                print(f"\n[{category.capitalize()}]")
                for key, info in items.items():
                    value = info.get("value", "")
                    timestamp = info.get("timestamp", "unknown")
                    print(f"{key}: {value} (saved at {timestamp})")
                has_memory = True

        if not has_memory:
            print("I don't remember anything yet.")

    def search(self):
        query = input("What do you want to search for? ").strip().lower()
        if not query:
            print("Search query cannot be empty.")
            return
        
        found = False
        for category, items in self.memory.items():
            results = {k:v for k, v in items.items() if query in k.lower() or query in v.get("value", "").lower()}
            if results:
                print(f"\n[{category.capitalize()}]")
                for k, v in results.items():
                    print(f"{k}: {v['value']} (saved at {v['timestamp']})")
                found = True

        if not found:
            print("There are no matching memories.")

    # where to update, verify category exists, ask what to update, ask for new value and save
    # self.memory[category][key] = updated_value
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
        
        entry = self.memory[category][key]

        choice = input("Update (k)ey, (v)alue, or (b)oth? ").strip().lower()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if choice == "v":
            updated_value = input(f"What should '{key}' be updated to? ").strip()
            if not updated_value:
                print("Value cannot be empty.")
                return

            entry["value"] = updated_value
            entry["timestamp"] = timestamp
        
        elif choice == "k":
            updated_key = input(f"What's the new key's name? ").strip()
            if not updated_key:
                print("Key cannot be empty")
                return
            
            if updated_key in self.memory[category]:
                print("This key already exists.")
                return
            
            self.memory[category][updated_key] = entry
            self.memory[category][updated_key]["timestamp"] = timestamp
            del self.memory[category][key]
        
        elif choice == "b":
            updated_key = input("New key name: ").strip()
            updated_value = input("New value: ").strip()

            if not updated_key or not updated_value:
                print("Key and value cannot be empty.")
                return
            
            if updated_key in self.memory[category]:
                print("That key already exists.")
                return
            
            self.memory[category][updated_key] = {
                "value": updated_value,
                "timestamp": timestamp
            }
            del self.memory[category][key]

        else:
            print("Invalid choice")
            return

        self.save_memory()
        print(f"Updated successfully.")

    # delete function answers similar questions as updating the value - ending action is just different
    # verify category and key exist, is the new value valid, overwrite value and save
    def delete(self):
        category = input("What category should I delete from? ").strip().lower()

        if category not in self.memory:
            print("Category does not exist.")
            return

        key = input("What key should I delete? ").strip()
        if not key:
            print("Key cannot be empty.")
            return
        
        if key not in self.memory[category]:
            print("That does not exist.")
            return
        
        delete_confirmation = input("Are you sure? (y/n): ").lower()
        if delete_confirmation != "y":
            return

        del self.memory[category][key]
        self.save_memory()
        print(f"I've deleted '{key}' from {category}.")
        