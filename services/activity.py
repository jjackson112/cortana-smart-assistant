# how Cortana behaves as not just when data exists with timestamps
# central activity service + exposes records
# create a Blueprint - GET
# where will the activity live - memory or persistence?

from flask import Blueprint, request, jsonify
from extensions import db
from models import Contacts, Inventory, Schedule, Todos

activity_bp = Blueprint("activity", __name__, url_prefix='/api/activity')

# each activity for each mode (CRUD) gets its own endpoint

# Contacts
@activity_bp.route("/contacts", methods=["POST"])
def create_contact():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    required_fields = ["mode", "name", "phone", "job"]
    missing = [f for f in required_fields if f not in data]

    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    contact = Contacts(
        mode = data["mode"],
        name = data["name"],
        phone = data["phone"],
        job = data["job"]
    )

    db.session.add(contact)
    db.session.commit()

    return jsonify(contact.to_dict()), 201

@activity_bp.route("/contacts", methods=["GET"])
def get_contact():
    mode = request.args.get("mode")

    query = Contacts.query
    if mode:
        query = query.filter_by(Contacts.date_added.desc()).all()

    contacts = query.all()
    return jsonify([c.to_dict() for c in contacts])

# PATCH applies changes while PUT replaces everything
@activity_bp.route("/contacts/<int:id>", methods=["PATCH"])
def update_contact(id): # a single resource, not a collection
    contact = Contacts.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # For each allowed field, if the client sent it, update that attribute on the database object - no hardcoding
    # no if "mode" in data: contact.mode = data["mode"] - less error prone + more concise
    for field in ["mode", "name", "phone", "job"]:
        if field in data:
            setattr(contact, field, data[field])

    db.session.commit()
    return jsonify(contact.to_dict())

@activity_bp.route("/contacts/<int:id>", methods=["DELETE"])
def delete_contact(id):
    contact = Contacts.query.get_or_404(id)

    db.session.delete(contact)
    db.session.commit()

    return "", 204

# Inventory
@activity_bp.route("/inventory", methods=["POST"])
def add_inventory():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    required_fields = ["mode", "category", "key", "value"]
    missing = [f for f in required_fields if f not in data]

    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    inventory = Inventory(
        mode = data["mode"],
        category = data["category"],
        key = data["key"],
        value = data["value"]
    )

    db.session.add(inventory)
    db.session.commit()

    return jsonify(inventory.to_dict()), 201

@activity_bp.route("/inventory", methods=["GET"])
def get_inventory():
    mode = request.args.get("mode")

    query = Inventory.query
    if mode:
        query = query.filter_by(mode=mode)

    inventory = query.all()
    return jsonify([i.to_dict() for i in inventory])

@activity_bp.route("/inventory/<int:id>", methods=["PATCH"])
def update_inventory(id): 
    inventory = Inventory.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    for field in ["mode", "category", "key", "value", "date_added"]:
        if field in data:
            setattr(inventory, field, data[field])

    db.session.commit()
    return jsonify(inventory.to_dict())

@activity_bp.route("/inventory/<int:id>", methods=["DELETE"])
def delete_inventory(id):
    inventory = Inventory.query.get_or_404(id)

    db.session.delete(inventory)
    db.session.commit()

    return "", 204

# Schedule

# To do 
@activity_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.json

    if not data or "mode" not in data or "name" not in data:
        return jsonify({"error": "Invalid JSON"}), 400

    todo = Todos(
        mode=data["mode"],
        name=data["name"]
    )

    db.session.add(todo)
    db.session.commit()

    return jsonify(todo.to_dict()), 201

@activity_bp.route("/todos", methods=["GET"])
def get_todos():
    mode = request.args.get("mode")

    todos = Todos.query.filter_by(mode=mode).all()

    return jsonify([t.to_dict() for t in todos])

@activity_bp.route("/todos/<int:id>", methods=["PATCH"])
def update_todo(id):
    todo = Todos.query.get_or_404(id)

    todo.completed = True
    db.session.commit()

    return jsonify(todo.to_dict())

@activity_bp.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todos.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    return "", 204
