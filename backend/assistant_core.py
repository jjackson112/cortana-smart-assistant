# FSM logic - finite state machine (design systems that can be in one state at a time)
from modules.inventory import Inventory
from modules.to_do_list import ToDo

inventory = Inventory()
todo = ToDo()

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
            "state": "main menu" 
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
                    "What task should be deleted?",
                    [inventory.list_memory()]
                ],
                "state": "inventory_delete"
            }
        
    return {
        "messages": ["Unknown inventory command."],
        "state": "inventory_command"
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
                "state": "main menu" # set main menu state (UX improvement)
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