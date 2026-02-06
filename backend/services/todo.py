# not to bloat db or break state
# log semantic events - not just db ones
# Cortana is event-driven and this performs actions and triggers logs
# conversation is frontend + disappears on refresh

from extensions import db
from models import Todos
from services.activity_log import log_activity

def add_todo(name):
    todo = Todos(mode="todo", name=name)
    db.session.add(todo)
    db.session.commit()

    log_activity(
        action="todo_added",
        entity_type="todo",
        entity_id=todo.id,
        metadata={"name": name}
    )

    return todo

def update_todo(todo_id, new_text):
    todo = Todos.query.get(todo_id)
    if not todo:
        return None

    old_text = todo.name
    todo.name = new_text
    db.session.commit()

    log_activity(
        action="todo_updated",
        entity_type="todo",
        entity_id=todo.id,
        metadata={"from": old_text, "to": new_text}
    )

    return todo

def delete_todo(todo_id):
    todo = Todos.query.get(todo_id)
    if not todo:
        return None

    db.session.delete(todo)
    db.session.commit()
    
    log_activity(
        action="todo_deleted",
        entity_type="todo",
        entity_id=todo.id,
    )
