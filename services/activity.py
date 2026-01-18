# how Cortana behaves as not just when data exists with timestamps
# central activity service + exposes records
# create a Blueprint - GET
# where will the activity live - memory or persistence? - business logic

from flask import Blueprint, request, jsonify
from extensions import db
from models import Contacts, Inventory, Schedule, Todos
from utils.crud import apply_updates
from utils.validation import require_fields
from utils.response import success, error_response

activity_bp = Blueprint("activity", __name__, url_prefix='/api/activity')

# each activity for each mode (CRUD) gets its own endpoint - check routes for separate files
# GET requests don't need a request body - no JSON validation or request.get_json()



# To do 
@activity_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.json
    ok, error_message = require_fields(data, ["mode", "name"])

    if not ok:
        return error_response(error_message, 400)

    todo = Todos(**data)

    db.session.add(todo)
    db.session.commit()

    return success(todo.to_dict()), 201

@activity_bp.route("/todos", methods=["GET"])
def get_todos():
    mode = request.args.get("mode")

    todos = Todos.query.filter_by(mode=mode).all()

    return jsonify([t.to_dict() for t in todos])

@activity_bp.route("/todos/<int:id>", methods=["PATCH"])
def update_todo(id):
    todo = Todos.query.get_or_404(id)

    data = request.get_json()
    apply_updates(todo, data["completed"])

    db.session.commit()

    return jsonify(todo.to_dict())

@activity_bp.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todos.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    return success(None, 204)
