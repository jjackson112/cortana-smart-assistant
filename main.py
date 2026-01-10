from contacts import ContactList
from inventory import Inventory
from schedule import Scheduler
from todo import ToDo

# Main program loop
def main():
    assistant_name = "Cortana"
    username = "Jasmine"

    print(f"Hi {username}! I'm {assistant_name}. How may I help you?")

    commands = {
        "remember": inventory.remember,
        "list": inventory.list_memory,
        "search": inventory.search,
        "update": inventory.update,
        "delete": inventory.delete
    }

    while True:
        command = input("\nEnter a command (remember, list, search, update, delete, exit):").strip().lower()

        if command == "exit":
            print("Later Jasmine! 🤗")
            break

        action = commands.get(command)
        if action:
            action() # call method
        else:
            print("I don't understand that command.")

    if __name__ == "__main__":
        main()