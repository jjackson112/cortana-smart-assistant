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

    def greeting(self):
        print(f"Hi, my name is {self.name}")

    def list_memory(self):
        if not self.memory:
            print("I don't remember this.")
        else:
            for key, value in self.memory.items():
                print(f"{key}: {value}")

if __name__ == "__main__":
    cortana = Cortana("Cortana")
    cortana.greeting()

# boolean
    while True:
        command = input("Enter a command (remember, list, exit):").lower()
        
        if command == "exit":
            print("Bye!")
            break

        elif command == "remember":
            key = input("What should I remember? ")
            value = input(f"What is '{key}'? ")
            cortana.memory[key] = value
            cortana.save_memory()
            print(f"\nGot it! I'll remember {key}.")

        elif command == "list":
            cortana.list_memory()

        elif command == "search":
            query = input("What do you want to search for?")
            results = {k:v for k,v in cortana.memory.items() if query.lower() in k.lower()}
            if results:
                for k,v in results.items():
                    print(f"{k}: {v}")
        else: 
            print("There are no matching memories.")

        else:
            print("I don't understand that command.")    
