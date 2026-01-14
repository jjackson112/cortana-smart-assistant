# how Cortana behaves as not just when data exists with timestamps
# central activity service + exposes records
# create a Blueprint - GET
# where will the activity live - memory or persistence?

from flask import Blueprint, request, jsonify
from app import db
from models import Contacts

activity_bp = Blueprint("activity", __name__, url_prefix='/api/activity')

# each activity for each mode (CUD -no R) gets its own endpoint

@activity_bp.route("/contacts", methods=["POST"])
def create_contact():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    required_fields = ["mode", "name", "phone", "job"]
    missing = [f for f in required_fields if f not in data]

    # missing = []
        # for f in required_fields:
        # if f not in data:
        # missing.append(f)

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