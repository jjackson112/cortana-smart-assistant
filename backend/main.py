from modules.contact_list import ContactList
from modules.inventory import Inventory
from modules.scheduler import Scheduler
from modules.to_do_list import ToDo

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

        select_mode = input("Type in the number to select an option ").strip()

        if select_mode == "1":
            contact_list_mode(contacts)
        
        elif select_mode == "2":
            inventory_mode(inventory)

        elif select_mode == "3":
            schedule_mode(scheduler)

        elif select_mode == "4":
            to_do_list_mode(todo)

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

def inventory_mode(inventory):
    print("\nLet's check the inventory 📋💻")

    commands = {
        "remember": inventory.remember,
        "list": inventory.list_memory,
        "search": inventory.search,
        "update": inventory.update,
        "delete": inventory.delete
    }

    while True:
        command = input("\nInventory command (remember, list, search, update, delete, main menu): ").strip().lower()

        if command == "main menu":
            print("\nReturning to main menu...\n")
            break

        action = commands.get(command)
        if action:
            action()
        else:
            print("Unknown inventory command.")

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

def to_do_list_mode(todo, input_text=None, state=None):

    if state is None:
        return {
            "messages": [
                "What's on the to do list? 📝",
                "To do list command (add, list, update, delete, main menu):"
            ],
            "state": "todo_command"
        }
        
    if state == "todo_command":
        if input_text == "main menu":
            return {
                "messages": ["Returning to main menu..."],
                "state": None
            }
        
    if input_text == "add":
        return {
            "messages": ["What would you like to add?"],
            "state": "todo_add_task"
        }
    
    if state == "todo_add_task":
        result = todo.add_task(input_text)
        return {
            "messages": [result],
            "state": "todo_command"
        }

    if input_text == "list":
        tasks = todo.show_list()
        return {
            "messages": tasks if tasks else["Your to do list is empty."],
            "state": "todo_command"
        }
    
    if input_text == "update":
        return {
            "messages": 
                ["What task would you like to update?",
                *todo.show_list()
            ],
            "state": "todo_update_task"
        }
    
    if state == "todo_update_task":
        if not input_text.isdigit():
            return {
                "messages": ["Please enter a valid task number."],
                "state": "todo_update_task"
            }
        
    
    if input_text == "delete":
        return {
            "messages": [
                "What task should be deleted?",
                *todo.show_list()
            ],
            "state": "todo_delete_task"
        }
    
    return {
        "messages" : ["Unknown to do list command."],
        "state": "todo_command"
    }

if __name__ == "__main__":
    main()