from flask import Blueprint, request
from extensions import db
from models import Todos
from utils.crud import apply_updates
from utils.validation import require_fields
from utils.response import success, error_response
from services.activity import log_activity

todo_bp = Blueprint("todo", __name__, url_prefix='/api/todo')

@todo_bp.route("/", methods=["POST"])
def create_todo():
    data = request.json
    ok, error_message = require_fields(data, ["mode", "name"])

    if not ok:
        return error_response(error_message, 400)

    todo = Todos(**data)

    db.session.add(todo)
    db.session.commit()

    return success(todo.to_dict()), 201

@todo_bp.route("/", methods=["GET"])
def get_todos():
    mode = request.args.get("mode")

    todos = Todos.query.filter_by(mode=mode).all()

    return success([t.to_dict() for t in todos])

@todo_bp.route("/<int:id>", methods=["PATCH"])
def update_todo(id):
    todo = Todos.query.get_or_404(id)

    data = request.get_json()
    apply_updates(todo, data["completed"])

    db.session.commit()

    return success(todo.to_dict())

@todo_bp.route("/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todos.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    return "", 204