from modules.contact_list import ContactList
from modules.inventory import Inventory
from modules.scheduler import Scheduler

# Main program loop (COMMAND ROUTER)
def main():
    assistant_name = "Cortana"
    username = "Jasmine"

    contacts = ContactList()
    scheduler = Scheduler()

    print(f"Hi {username}! I'm {assistant_name}. How may I help you?\n")

    while True:
        print("1. Contact List")
        print("2. Inventory")
        print("3. Schedule")
        print("4. To Do List")
        print("5. Exit")

        select_mode = input("Type in the number to select an option ").strip()

        if select_mode == "1":
            contact_list_mode(contacts)

        elif select_mode == "3":
            schedule_mode(scheduler)

        elif select_mode == "5":
            print(f"See you next time {username}! 🤗")
            break

        else:
            print("Invalid selection.")
            continue # return kills the program
        
def contact_list_mode(contacts):
    print("\nLet's head to the contact list 📲📞☎️")

    commands = {
        "add": contacts.add_contacts_prompt,
        "search": contacts.search_contacts,
        "update": contacts.update_contacts,
        "delete": contacts.delete_contacts
    }

    while True:
        command = input("\nContact list command (add, search, update, delete, main menu): ").strip().lower()

        if command == "main menu" :
            print("\nReturning to main menu...\n")
            break

        action = commands.get(command)
        if action:
            action()
        else:
            print("Unknown contact list command.")

def schedule_mode(scheduler):
    print("What's up with the schedule? 📅")

    commands = {
        "add": scheduler.add_events,
        "list": scheduler.list_events,
        "search": scheduler.search_events,
        "update": scheduler.update_events,
        "delete": scheduler.delete_event
    }

    while True:
        command = input("\nSchedule command (add, list, search, update, delete, main menu): ").strip().lower()

        if command == "main menu":
            print("\nReturning to main menu...\n")
            break

        action = commands.get(command)
        if action:
            action()
        else:
            print("Unknown schedule command.")

if __name__ == "__main__":
    main()