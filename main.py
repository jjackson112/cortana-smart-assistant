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

        if select_mode == "1":
            contact_list_mode()
        
        elif select_mode == "2":
            inventory_mode()

        elif select_mode == "3":
            schedule_mode()

        elif select_mode == "4":
            to_do_list_mode()

        elif select_mode == "5":
            print("See you next time {username}! 🤗")
            break

        else:
            print("Invalid selection.")
            return
        
def contact_list_mode():
    print("\nLet's head to the contact list 📲📞☎️")

    commands = {
        "add": contacts.add_contacts,
        "search": contacts.search_contacts,
        "update": contacts.update_contacts,
        "delete": contacts.delete_contacts
    }

    while True:
        command = input("\nContact list command (add, search, update, delete, back): ").strip().lower()

        if command == "back":
            break

        action = commands.get(command)
        if action:
            action()
        else:
            print("Unknown contact list command.")

def inventory_mode():
    print("\nLet's check the inventory 📋💻")

    commands = {
        "remember": inventory.remember,
        "list": inventory.list_memory,
        "search": inventory.search,
        "update": inventory.update,
        "delete": inventory.delete
    }

    while True:
        command = input("\nInventory command (remember, list, search, update, delete, back): ").strip().lower()

        if command == "back":
            break

        action = commands.get(command)
        if action:
            action()
        else:
            print("Unknown inventory command.")

def schedule_mode():
    print("What's up with the schedule? 📅")

def to_do_list_mode():
    print("What's on the to do list? 📝")

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