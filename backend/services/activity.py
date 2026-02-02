# how Cortana behaves as not just when data exists with timestamps
# central activity service + exposes records services = business logic
# create a Blueprint - GET
# where will the activity live - memory or persistence? - business logic - how to create what the user wants

from flask import Blueprint, request
from backend.models import ActivityLog
from utils.response import success
from services.activity_retention import prune_activity_log

activity_bp = Blueprint("activity", __name__, url_prefix='/api/activity')

# each activity for each mode (CRUD) gets its own endpoint - check routes for separate files
# GET requests don't need a request body - no JSON validation or request.get_json()
# No CRUD, models, db, or validation - better organization

@activity_bp.route("/", methods=["GET"])
def list_activities():
    query = ActivityLog.query

    mode = request.args.get("mode")
    entity_type = request.args.get("entity_type")
    action = request.args.get("action")

    if mode:
        query = query.filter_by(mode=mode)
    if entity_type:
        query = query.filter_by(entity_type=entity_type)
    if action:
        query = query.filter_by(action=action)

    activities = query.order_by(ActivityLog.timestamp.desc()).all()
    return success([a.to_dict() for a in activities])

@activity_bp.route("/", methods=["POST"])
def create_activity():
    data = request.get_json()
    if not data:
        return {"error": "No data provided"}, 400

    required_fields = ["mode", "entity_type", "action"]
    if not all(field in data for field in required_fields):
        return{"error": "Missing required fields"}, 400
    
    activity = ActivityLog(
        mode=data["mode"],
        entity_type=data["entity_type"],
        action=data["action"],
        details=data.get("details")
    )
    activity.save()

    # Optional: prune old entries automatically
    prune_activity_log()
    
    return success(activity.to_dict())

@activity_bp.route("/prune_activity", methods=["DELETE"])
def prune_activities():
    deleted_activity = prune_activity_log()
    return success({"deleted": deleted_activity})
