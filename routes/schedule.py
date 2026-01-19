from flask import Blueprint, request
from extensions import db
from models import Schedule
from utils.crud import apply_updates
from utils.validation import require_fields
from utils.response import success, error_response
from services.activity import log_activity

schedule_bp = Blueprint("schedule", __name__, url_prefix='/api/schedule')

@schedule_bp.route("/", methods=["POST"])
def create_event():
    data = request.get_json()
    ok, error_message = require_fields(data, ["mode", "type", "description", "date", "time"])

    if not ok:
        return error_response(error_message, 400)

    event = Schedule(**data)

    db.session.add(event)
    db.session.commit()

    log_activity(
        action="created_event",
        entity_type="event",
        entity_id=event.id,
        metadata={"type": event.type, "date": event.date}
    )

    return success(event.to_dict()), 201

@schedule_bp.route("/", methods=["GET"])
def list_events():
    mode = request.args.get("mode")

    query = Schedule.query
    if mode:
        query = query.filter_by(mode=mode)

    events = query.order_by(Schedule.date_added.desc()).all()
    return success([e.to_dict() for e in events])

@schedule_bp.route("/<int:id>", methods=["PATCH"])
def update_event(id): # a single resource, not a collection
    event = Schedule.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return error_response("Invalid JSON", 400)
    
    apply_updates(
        event,
        data,
        ["mode", "type", "description", "date", "time"]
    )

    db.session.commit()

    log_activity(
        action="updated",
        entity_type="schedule",
        entity_id=event.id,
        metadata=data
    )

    return success(event.to_dict())

@schedule_bp.route("/<int:id>", methods=["DELETE"])
def delete_event(id):
    event = Schedule.query.get_or_404(id)

    db.session.delete(event)
    db.session.commit()

    log_activity(
        action="deleted",
        entity_type="schedule",
        entity_id=id
    )

    return "", 204
