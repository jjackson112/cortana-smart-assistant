from flask import Blueprint, request
from extensions import db
from models import Todos
from utils.crud import apply_updates
from utils.validation import require_fields
from utils.response import success, error_response
from services.activity_log import log_activity

todo_bp = Blueprint("todo", __name__, url_prefix='/api/todo')

@todo_bp.route("/", methods=["POST"])
def create_todo():
    data = request.get_json()

    if not data:
        return error_response("Invalid JSON", 400)
    
    ok, error_message = require_fields(data, ["mode", "name"])

    if not ok:
        return error_response(error_message, 400)

    todo = Todos(**data)

    db.session.add(todo)
    db.session.commit()

    log_activity(
        action="created_todo",
        entity_type="todo",
        entity_id=todo.id,
        metadata={"name": todo.name}
    )

    return success(todo.to_dict()), 201

@todo_bp.route("/", methods=["GET"])
def list_todos():
    mode = request.args.get("mode")
    query = Todos.query
    if mode:
        query = query.filter_by(mode=mode)

    todos = query.all()
    return success([t.to_dict() for t in todos])

@todo_bp.route("/<int:id>", methods=["PATCH"])
def update_todo(id):
    todo = Todos.query.get_or_404(id)

    data = request.get_json()
    if not data:
        return error_response("Invalid JSON", 400)
    
    apply_updates(todo, data["completed"])

    db.session.commit()

    log_activity(
        action="created_todo",
        entity_type="todo",
        entity_id=todo.id,
        metadata=data
    )

    return success(todo.to_dict())

@todo_bp.route("/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todos.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    log_activity(
        action="deleted",
        entity_type="todo",
        entity_id=id
    )

    return "", 204