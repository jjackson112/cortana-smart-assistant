# What will Cortana do as my assistant?
# She should be a program that can remember and respond

# while loop (conditionals) - command loop
# runs until condition is met - control structure
# for key, value lists everything in memory
# for loop for inside commands or methods

import json
from datetime import datetime
from pathlib import Path

class Inventory:
    def __init__(self):
        self.memory_path = self.get_memory_path()
        self.ensure_data_folder()
        self.memory = self.load_memory()

    # Categories setup
        for category in ["personal", "work", "other"]:
            self.memory.setdefault(category, {})

    # Ensure the data folder exists
    def ensure_data_folder(self):
        data_folder = self.memory_path.parent
        data_folder.mkdir(parents=True, exist_ok=True)

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
        #  Use Path for easier handling
        base_path = Path(__file__).parent.parent
        return base_path / "data" / "memory.json"    
    
    # Commands
    def remember(self, category, key, value):
        category = category.lower()
        if category not in self.memory:
            category = "other"
            return "Unknown category, using 'other'."
            
        if not key or not value:
            return "Key and value cannot be empty!"
        
        # Timestamp added
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.memory[category][key] = {"value": value, "timestamp": timestamp}

        self.save_memory()
        return f"Got it! I'll remember '{key}' in {category}."
            
    def list_memory(self):
        output = []
        for category, items in self.memory.items():
            if items:
                output.append(f"\n[{category.capitalize()}]")
                for key, info in items.items():
                    value = info.get("value", "")
                    timestamp = info.get("timestamp", "unknown")
                    output.append(f"{key}: {value} (saved at {timestamp})")

        return "\n".join(output) if output else "I don't remember anything yet."

    def search(self, query):
        if not query:
            return "Search query cannot be empty."
        
        query = query.lower()
        output = []
        for category, items in self.memory.items():
            results = {k:v for k, v in items.items() if query in k.lower() or query in v.get("value", "").lower()}
            if results:
                output.append(f"\n[{category.capitalize()}]")
                for k, v in results.items():
                    output.append(f"{k}: {v['value']} (saved at {v['timestamp']})")
        return "\n".join(output) if output else "There are no matching entries."

    # where to update, verify category exists, ask what to update, ask for new value and save
    # self.memory[category][key] = updated_value
    def update(self):
        category = input("What category needs to be updated? ").strip().lower()

        if category not in self.memory:
            return "Category does not exist."

        key = input("What should I update? ").strip()
        if not key:
            return "Key cannot be empty."
        
        if key not in self.memory[category]:
            return "That does not exist."
        
        entry = self.memory[category][key]

        choice = input("Update (k)ey, (v)alue, or (b)oth? ").strip().lower()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if choice == "v":
            updated_value = input(f"What should '{key}' be updated to? ").strip()
            if not updated_value:
                return "Value cannot be empty."

            entry["value"] = updated_value
            entry["timestamp"] = timestamp
        
        elif choice == "k":
            updated_key = input(f"What's the new key's name? ").strip()
            if not updated_key:
                return "Key cannot be empty"
            
            if updated_key in self.memory[category]:
                return "This key already exists."
            
            self.memory[category][updated_key] = entry
            self.memory[category][updated_key]["timestamp"] = timestamp
            del self.memory[category][key]
        
        elif choice == "b":
            updated_key = input("New key name: ").strip()
            updated_value = input("New value: ").strip()

            if not updated_key or not updated_value:
                return "Key and value cannot be empty."
            
            if updated_key in self.memory[category]:
                return "That key already exists."
            
            self.memory[category][updated_key] = {
                "value": updated_value,
                "timestamp": timestamp
            }
            del self.memory[category][key]

        else:
            return "Invalid choice"

        self.save_memory()
        return f"Updated successfully."

    # delete function answers similar questions as updating the value - ending action is just different
    # verify category and key exist, is the new value valid, overwrite value and save
    def delete(self, category, key, confirm=False):
        category = category.lower()

        if category not in self.memory:
            return "Category does not exist."
        
        if key not in self.memory[category]:
            return "That does not exist."
        
        if not confirm: 
            return f"Are you sure you want to delete '{key}' from {category}? (y/n)"

        del self.memory[category][key]
        self.save_memory()
        return f"I've deleted '{key}' from {category}."
        