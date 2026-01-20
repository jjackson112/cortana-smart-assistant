# business logic - separation of concerns from activity_bp (HTTP)

from extensions import db
from models import ActivityLog

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