# how Cortana behaves as not just when data exists with timestamps
# central activity service + exposes records
# create a Blueprint - GET
# where will the activity live - memory or persistence?

from flask import Blueprint, request, jsonify
from app import db
from models import Contacts

activity_bp = Blueprint("activity", __name__, url_prefix='/api/activity')

# each activity for each mode (CRUD) gets its own endpoint

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
        query = query.filter_by(mode=mode)

    contacts = query.all()
    return jsonify([c.to_dict() for c in contacts])

@activity_bp.route("/contacts/<int:id>", methods=["PATCH"])
def update_contact(id): # a single resource, not a collection
    contact = Contacts.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    db.session.commit()
    return jsonify(contact.to_dict())

@activity_bp.route("/contacts/<int:id>", methods=["DELETE"])
def delete_contact(id):
    contact = Contacts.query.get_or_404(id)

    db.session.delete(contact)
    db.session.commit()

    return "", 204