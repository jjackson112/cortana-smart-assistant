# What will Cortana do as my assistant?
# She should be a program that can remember and respond

# while loop (conditionals) - command loop
# runs until condition is met - control structure
# for key, value lists everything in memory
# for loop for inside commands or methods

class Cortana:
    def __init__(self, name):
        self.name = name
        self.memory = {}

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



