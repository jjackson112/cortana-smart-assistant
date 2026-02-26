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

def contact_mode(input_text=None, state=None):
    if input_text:
        input_text = input_text.strip().lower()

    if state is None:
        return {
            "messages": [
            "Let's head to the contact list 📲📞☎️",
            "Contact list commands (add, search, update, delete, main menu):"
            ],
            "state": "contact_command"
        }

    if input_text == "main menu":
        return {
            "messages": [
                "Returning to main menu...",
                "Let's head to the contact list 📲📞☎️",
                "Contact list commands (add, search, update, delete, main menu):"],
            "state": "contact_command" 
        }
    
    if state == "contact_command":
        if input_text == "add":
            return {
                "messages": [
                    "Enter name, phone number, and job separated by commas."
                ],
                "state": "contact_add"
            }

        if input_text == "search":
            return {
                "messages": [
                    "Enter a name or job to search."
                ],
                "state": "contact_search"
            }

        if input_text == "update":
            return {
                "messages": [
                    "Enter contact name to update."
                ],
                "state": "contact_update"
            }

        if input_text == "delete":
            return {
                "messages": [
                    "Enter contact name to delete."
                ],
                "state": "contact_delete"
            }
    
    if state == "contact_add":
        try:
            name, phone, job = [x.strip() for x in input_text.split(",")]
        except:
            return {
                "messages": ["Invalid format. Use: name, phone, job."],
                "state": "contact_add"
            }

        result = contacts.add_contacts(name, phone, job)
        return {
            "messages": [result],
            "state": "contact_command"
        }

    if state == "contact_search":
        results = contacts.search_contacts(input_text)

        if not results:
            return {
                "messages": ["No contacts found."],
                "state": "contact_command"
            }
        
        formatted = [
            f"{c['name']} | {c['phone_number']} | {c['job']}"
            for c in results
        ]

        return {
            "messages": formatted,
            "state": "contact_command"
        }
    
    if state == "contact_update":
        return {
            "messages": ["Enter the name of the contact you want to update."],
            "state": "contact_update_select"
        }

    if state == "contact_update_select":
        selected_name = input_text
        return {
            "messages": ["Enter new phone number and job separated by commas."],
            "state": f"contact_update_data:{selected_name}"
        }

    if state and state.startswith("contact_update_data:"):
        selected_name = state.split(":")[1]

        try:
            phone, job = [x.strip() for x in input_text.split(",")]
        except:
            return {
                "messages": ["Invalid format. Use: phone, job."],
                "state": state
            }

        result = contacts.update_contacts(selected_name, phone, job)

        return {
            "messages": [result],
            "state": "contact_command"
        }
    
    if state == "contact_delete":
        result = contacts.delete_contacts(input_text, confirm=True)
        return {
            "messages": [result],
            "state": "contact_command"
        }   
    
    return {
        "messages": ["Unknown contact command"],
        "state": "contact_command"
    }

def inventory_mode(input_text=None, state=None):
    if input_text:
        input_text = input_text.strip().lower()

    if state is None:
        return {
            "messages": [
                "Let's check the inventory 📋💻",
                "Inventory commands (remember, list, search, update, delete, main menu):"
            ],
            "state": "inventory_command"
        }

    if input_text == "main menu":
        return {
            "messages": [
                "Returning to main menu...",
                "Let's check the inventory 📋💻",
                "Inventory commands (remember, list, search, update, delete, main menu):"],
            "state": "inventory_command" 
        }
    
    if state == "inventory_command":
        if input_text == "remember":
            return {
                "messages": ["What would you like to add?"],
                "state": "inventory_add"
            }

        if input_text == "list":
            items = inventory.list_memory()

            return {
                "messages": [items] if items else ["Your inventory is empty."],
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
            "What's up with the schedule? 📅",
            "Schedule commands (add, list, search, update, delete, main menu):"
            ],
            "state": "schedule_command"
        }

    if input_text == "main menu":
        return {
            "messages": [
                "Returning to main menu...",
                "What's up with the schedule? 📅",
                "Schedule commands (add, list, search, update, delete, main menu):"],
            "state": "schedule_command" 
        }
    if state == "schedule_command":
        if input_text == "add":
            return {
                "messages": ["Enter title, type(meeting/reminder), description, date(MM-DD-YYYY), time(HH:MM) separated by commas."],
                "state": "schedule_add"
            }
        
        if input_text == "list":
            events = schedule.list_events()
            if not events:
                return {
                    "messages": ["No events found."],
                    "state": "schedule_command"
                }
            
            formatted = [
                f"{e['title']} ({e['type']}) - {e['date']} {e['time']}"
                for e in events
            ]

            return {
                "messages": formatted,
                "state": "schedule_command"
            }
        
        if input_text == "search":
            return {
                "messages": ["Enter title or type to search."],
                "state": "schedule_search"
            }
        
        if input_text == "update":
            return {
                "messages": ["Enter the title of the event to update."],
                "state": "schedule_update_select"
            }

        if input_text == "delete":
            return {
                "messages": ["Enter the title of the event to delete."],
                "state": "schedule_delete"
            }

    if state == "schedule_add":
        try:
            title, event_type, description, date, time = [
                x.strip() for x in input_text.split(",")
            ]
        except:
            return {
                "messages": ["Invalid format. Please try again."],
                "state": "schedule_add"
            }

        result = schedule.add_events(title, event_type, description, date, time)

        return {
            "messages": [result],
            "state": "schedule_command"
        }
    
    if state == "schedule_search":
        results = schedule.search_events(input_text)

        if not results:
            return {
                "messages": ["No matching events found."],
                "state": "schedule_command"
            }

        formatted = [
                f"{e['title']} ({e['type']}) - {e['date']} {e['time']}"
                for e in results
            ]

        return {
            "messages": formatted,
            "state": "schedule_command"
        }

    if state == "schedule_update_select":
        return {
            "messages": ["Enter new type, description, date, time separated by commas."],
            "state": f"schedule_update_data:{input_text}"
        }

    if state and state.startswith("schedule_update_data:"):
        old_title = state.split(":")[1]

        try:
            event_type, description, date, time = [
                x.strip() for x in input_text.split(",")
            ]
        except:
            return {
                "messages": ["Invalid format. Use: type, description, date, time."],
                "state": state
            }

        result = schedule.update_events(old_title, event_type, description, date, time)

        return {
            "messages": [result],
            "state": "schedule_command"
        }

    if state == "schedule_delete":
        result = schedule.delete_events(input_text)
        return {
            "messages": [result],
            "state": "schedule_command"
        }

    return {
        "messages": ["Unknown schedule command"],
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
                    "To do list commands (add, list, update, delete, main menu):"],
                "state": "todo_command" # set main menu state (UX improvement)
            }

    if state is None:
        return {
            "messages": [
                "What's on the to do list? 📝",
                "To do list commands (add, list, update, delete, main menu):"
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
    "contacts": contact_mode,
    "inventory": inventory_mode,
    "schedule": schedule_mode,
    "todo": to_do_list_mode
}

# Frontend  →  Flask Route  →  handle_command()  →  Mode Handler
def handle_command(input_text=None, state=None):
    # ensures the state is always a dict with keys 'mode' and 'state'
    if state is None:
        state = {"mode": None, "state": None}

    # normalize empty string to None
    if not state.get("mode"):
        state["mode"] = None

    current_mode = state.get("mode")
    current_substate = state.get("state")

    # normal FSM handling - input_text is the mode name, always switch modes
    if input_text in MODE_HANDLERS:
        handler = MODE_HANDLERS[input_text]
        result = handler(None, None) # initialize mode
        return {
            "messages": result["messages"],
            "state": {
                "mode": input_text, 
                "state": result["state"]
            }
        }
    
    # fallback if no mode is selected
    if current_mode is None:
        return {
            "messages": ["No active mode selected"], 
            "state": state
        }
    
    # Otherwise route to active mode
    handler = MODE_HANDLERS[current_mode]
    result = handler(input_text, current_substate)

    return {
        "messages": result["messages"],
        "state": {
            "mode": current_mode,
            "state": result["state"]
        }
    }