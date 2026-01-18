# how Cortana behaves as not just when data exists with timestamps
# central activity service + exposes records services = business logic
# create a Blueprint - GET
# where will the activity live - memory or persistence? - business logic - how to create what the user wants

from flask import Blueprint
from extensions import db
from models import ActivityLog

activity_bp = Blueprint("activity", __name__, url_prefix='/api/activity')

# each activity for each mode (CRUD) gets its own endpoint - check routes for separate files
# GET requests don't need a request body - no JSON validation or request.get_json()
# No CRUD, models, db, or validation - better organization

# log activity
def log_activity(action, entity_type, entity_id=None, metadata=None):
    activity = ActivityLog(
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        metadata=metadata
    )
    db.session.add(activity)
    db.session.commit()