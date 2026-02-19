# FSM logic - finite state machine (design systems that can be in one state at a time)
# startswith() checks whether a string starts with a specific substring

from modules.contact_list import ContactList
from modules.inventory import Inventory
from modules.scheduler import Scheduler
from modules.to_do_list import ToDo

contacts = ContactList()
inventory = Inventory()
schedule = Scheduler()
todo = ToDo()

def contact_list_mode(input_text=None, state=None):
    if input_text:
        input_text = input_text.strip().lower()

    if state is None:
        return {
            "messages": [
            "Let's head to the contact list 📲📞☎️"
            ],
            "state": "contact_list_command"
        }

    if input_text == "main menu":
        return {
            "messages": [
                "Returning to main menu...",
                "Let's head to the contact list 📲📞☎️",
                "Contact list command (add, search, update, delete, main menu):"],
            "state": "contact_list_command" 
        }
    if state == "contact_list_command":
        if input_text == "add":
            return {
                "messages": ,
                "state": "contact_list_command"
            }

        if input_text == "search":
            return {
                "messages": ,
                "state": "contact_list_command"
            }

        if input_text == "update":
            return {
                "messages": ,
                "state": "contact_list_command"
            }

        if input_text == "delete":
            return {
                "messages": ,
                "state": "contact_list_command"
            }

def inventory_mode(input_text=None, state=None):
    if input_text:
        input_text = input_text.strip().lower()

    if state is None:
        return {
            "messages": [
                "Let's check the inventory 📋💻",
                "Inventory command (remember, list, search, update, delete, main menu):"
            ],
            "state": "inventory_command"
        }

    if input_text == "main menu":
        return {
            "messages": [
                "Returning to main menu...",
                "Let's check the inventory 📋💻",
                "Inventory command (remember, list, search, update, delete, main menu):"],
            "state": "inventory_command" 
        }
    
    if state == "inventory_command":
        if input_text == "remember":
            return {
                "messages": ["What would you like to add?"],
                "state": "inventory_add"
            }

        if input_text == "list":
            return {
                "messages": [inventory.list_memory()] if inventory else ["Your inventory is empty."],
                "state": "inventory_command"
            }
        
        if input_text == "search":
            return {
                "messages": ["What would you like to search for?"],
                "state": "inventory_search"
            }

        if input_text == "update":
            return {
                "messages": [
                    "What task would you like to update?",
                    *inventory.list_memory().split("\n")
                ],
                "state": "inventory_update"
            }

        if input_text == "delete":
            return {
                "messages": [
                    "What should be deleted?",
                    *inventory.list_memory().split("\n")
                ],
                "state": "inventory_delete"
            }
    
    if state == "inventory_add":
        return {
            "messages": ["Which category? (personal, work or other)"],
            "state": "inventory_add_category"
        }
    
    if state == "inventory_add_category":
        category = input_text.strip().lower()

        if category not in ["personal", "work"]:
            category = "other"

        return {
            "messages": ["What key should I remember?"],
            "state": f"inventory_add_key:{category}"
        }
    
    if state and state.startswith("inventory_add_key"):
        category = state.split(":")[1]
        key = input_text

        return {
            "messages": [f"What is the value of '{key}'?"],
            "state": f"inventory_add_value:{category}:{key}"
        } 

    if state and state.startswith("inventory_add_value:"):
        _, category, key = state.split(":")
        value = input_text

        msg = inventory.remember(category, key, value)

        return {
            "messages": [msg],
            "state": "inventory_command"
    }    
       
    return {
        "messages": ["Unknown inventory command."],
        "state": "inventory_command"
    }

def schedule_mode(input_text=None, state=None):
    if input_text:
        input_text = input_text.strip().lower()

    if state is None:
        return {
            "messages": [
            "What's up with the schedule? 📅"
            ],
            "state": "schedule_command"
        }

    if input_text == "main menu":
        return {
            "messages": [
                "Returning to main menu...",
                "What's up with the schedule? 📅",
                "Schedule command (add, list, search, update, delete, main menu):"],
            "state": "schedule_command" 
        }
    if state == "schedule_command":
        if input_text == "add":
            return {
                "messages": ,
                "state": "schedule_command"
            }
        
        if input_text == "list":
            return {
                "messages": [],
                "state": "schedule_command"
            }

        if input_text == "search":
            return {
                "messages": ,
                "state": "schedule_command"
            }

        if input_text == "update":
            return {
                "messages": ,
                "state": "schedule_command"
            }

        if input_text == "delete":
            return {
                "messages": ,
                "state": "schedule_command"
            }

def to_do_list_mode(input_text=None, state=None):
    if input_text:
        input_text = input_text.strip().lower()

    if input_text == "main menu":
            return {
                "messages": [
                    "Returning to main menu...",
                    "What's on the to do list? 📝",
                    "To do list command (add, list, update, delete, main menu):"],
                "state": "todo_command" # set main menu state (UX improvement)
            }

    if state is None:
        return {
            "messages": [
                "What's on the to do list? 📝",
                "To do list command (add, list, update, delete, main menu):"
            ],
            "state": "todo_command"
        }

    if state == "todo_command":
        if input_text == "add":
            return {
                "messages": ["What would you like to add?"],
                "state": "todo_add_task"
            }

        if input_text == "list":
            tasks = todo.show_list()
            return {
                "messages": tasks if tasks else ["Your to do list is empty."],
                "state": "todo_command"
            }

        if input_text == "update":
            return {
                "messages": [
                    "What task would you like to update?",
                    *todo.show_list()
                ],
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

    if state == "todo_add_task":
        result = todo.add_task(input_text)
        return {
            "messages": [result],
            "state": "todo_command"
        }

    if state == "todo_update_task":
        if not input_text.isdigit():
            return {
                "messages": ["Please enter a valid task number."],
                "state": "todo_update_task"
            }

        index = int(input_text) - 1
        return {
            "messages": ["What is the updated task?"],
            "state": f"todo_update_text:{index}"
        }

    if state and state.startswith("todo_update_text:"):
        index = int(state.split(":")[1])
        result = todo.update_task(index, input_text)
        return {
            "messages": [result],
            "state": "todo_command"
        }

    if state == "todo_delete_task":
        if not input_text.isdigit():
            return {
                "messages": ["Please enter a valid task number."],
                "state": "todo_delete_task"
            }

        index = int(input_text) - 1
        result = todo.delete_task(index)
        return {
            "messages": [result],
            "state": "todo_command"
        }

    return {
        "messages": ["Unknown to do list command."],
        "state": "todo_command"
    }

# map mode names to their handlers
MODE_HANDLERS = {
    "inventory": inventory_mode,
    "todo": to_do_list_mode
}

def handle_command(input_text=None, state=None):
    # ensures the state is always a dict with keys 'mode' and 'state'
    if state is None:
        state = {"mode": None, "state": None}

    current_mode = state.get("mode")

    # normal FSM handling
    if current_mode in MODE_HANDLERS:
        handler = MODE_HANDLERS[current_mode]
        result = handler(input_text, state.get("state"))
        return {
            "messages": result["messages"],
            "state": {"mode": current_mode, "state": result["state"]}
        }
    
    # fallback if no mode is selected
    return {"messages": ["No active mode selected"], "state": state}