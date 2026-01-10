from contacts import ContactList
from inventory import Inventory
from scheduler import Scheduler
from todo import ToDo

# Main program loop (COMMAND ROUTER)
def main():
    assistant_name = "Cortana"
    username = "Jasmine"

    inventory = Inventory()
    contacts = ContactList()
    scheduler = Scheduler()
    todo = ToDo()

    print(f"Hi {username}! I'm {assistant_name}. How may I help you?\n")

    while True:
        print("1. Contact List")
        print("2. Inventory")
        print("3. Schedule")
        print("4. To Do List")
        print("5. Exit")

        select_mode = input("Select an option").strip()

        commands = {
            # contacts
    
            # inventory
            "remember": inventory.remember,
            "list": inventory.list_memory,
            "search": inventory.search,
            "update": inventory.update,
            "delete": inventory.delete
    
            # schedule
    
            # to do list
        }
    
        while True:
            command = input("\nCommand (or exit): ").strip().lower()
    
            if command == "exit":
                print("Later {username}! 🤗")
                break
            
            action = commands.get(command)
            if action:
                action() # call method
            else:
                print("I don't understand that command.")
    
        if __name__ == "__main__":
            main()