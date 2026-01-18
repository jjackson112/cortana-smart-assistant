from flask import Flask, Blueprint, request, jsonify
from extensions import db
from models import Contacts
from utils.crud import apply_updates
from utils.validation import require_fields
from utils.response import success, error_response

contacts_bp = Blueprint("contacts", __name__, url_prefix="/api/contacts")

@contacts_bp.route("/contacts", methods=["POST"])
def create_contact():
    data = request.get_json()
    ok, error_message = require_fields(data, ["mode", "name", "phone", "job"])

    if not ok:
        return error_response(error_message, 400)

    contact = Contacts(**data)

    db.session.add(contact)
    db.session.commit()

    return success(contact.to_dict()), 201

@contacts_bp.route("", methods=["GET"])
def list_contact():
    mode = request.args.get("mode")

    query = Contacts.query
    if mode:
        query = query.filter_by(mode=mode) # filters keywords only

    # order_by sorts queries
    contacts = query.order_by(Contacts.date_added.desc()).all() # all() ends query
    return success([c.to_dict() for c in contacts])

# PATCH applies changes (partially) while PUT replaces everything
@contacts_bp.route("/<int:id>", methods=["PATCH"])
def update_contact(id): # a single resource, not a collection
    contact = Contacts.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return error_response("Invalid JSON", 400)
    
    apply_updates(
        contact,
        data,
        ["mode", "name", "phone", "job"]
    )

    db.session.commit()
    return success(contact.to_dict())

@contacts_bp.route("/<int:id>", methods=["DELETE"])
def delete_contact(id):
    contact = Contacts.query.get_or_404(id)

    db.session.delete(contact)
    db.session.commit()

    return success(None, 204)