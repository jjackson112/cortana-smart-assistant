from flask import Blueprint, request
from extensions import db
from models import Inventory
from utils.crud import apply_updates
from utils.validation import require_fields
from utils.response import success, error_response
from services.activity import log_activity

inventory_bp = Blueprint("inventory", __name__, url_prefix='/api/inventory')

@inventory_bp.route("/", methods=["POST"])
def create_inventory():
    data = request.get_json()
    if not data:
        return error_response("Invalid JSON", 400)

    ok, error_message = require_fields(data, ["mode", "category", "key", "value"])

    if not ok:
        return error_response(error_message, 400)

    inventory = Inventory(**data)

    db.session.add(inventory)
    db.session.commit()

    log_activity(
        action="created_inventory",
        entity_type="inventory",
        entity_id=inventory.id,
        metadata={"category": inventory.category, "key": inventory.key, "value": inventory.value}
    )

    return success(inventory.to_dict()), 201

@inventory_bp.route("/", methods=["GET"])
def list_inventory():
    mode = request.args.get("mode")

    query = Inventory.query
    if mode:
        query = query.filter_by(mode=mode)

    inventory = query.order_by(Inventory.date_added.desc()).all()
    return success([i.to_dict() for i in inventory])

@inventory_bp.route("/<int:id>", methods=["PATCH"])
def update_inventory(id): 
    inventory = Inventory.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return error_response("Invalid JSON", 400)

    apply_updates(
        inventory,
        data,
        ["mode", "category", "key", "value"]
    )

    db.session.commit()

    log_activity(
        action="updated",
        entity_type="inventory",
        entity_id=inventory.id,
        metadata=data
    )

    return success(inventory.to_dict())

@inventory_bp.route("/<int:id>", methods=["DELETE"])
def delete_inventory(id):
    inventory = Inventory.query.get_or_404(id)

    db.session.delete(inventory)
    db.session.commit()

    
    log_activity(
        action="deleted",
        entity_type="inventory",
        entity_id=id
    )

    return "", 204
