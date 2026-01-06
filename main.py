# What will Cortana do as my assistant?
# She should be a program that can remember and respond

# while loop (conditionals) - command loop
# runs until condition is met - control structure
# for key, value lists everything in memory
# for loop for inside commands or methods

import json

class Cortana:
    def __init__(self, name):
        self.name = name
        self.memory = self.load_memory()

    def load_memory(self):
        try:
            with open("memory.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Memory file corrupted. Starting fresh.")
            return {}
        
    def save_memory(self):
        with open("memory.json", "w") as file:
            json.dump(self.memory, file, indent=4)

    def greeting(self):
        print(f"Hi, my name is {self.name}")

    def list_memory(self):
        if not self.memory:
            print("I don't recall this.")
        else:
            for key, value in self.memory.items():
                print(f"{key}: {value}")

if __name__ == "__main__":
    cortana = Cortana("Cortana")
    cortana.greeting()

    while True:
        command = input("Enter a command (remember, list, exit):").lower()
        
        if command == "exit":
            print("Bye!")
            break

        elif command == "remember":
            key = input("What should I remember?")
            value = input(f"What is '{key}'?")
            cortana.memory[key] = value
            cortana.save_memory()
            print(f"Got it! I'll remember {key}.")

        elif command == "list":
            cortana.list_memory()

        else:
            print("I don't understand that command.")    



