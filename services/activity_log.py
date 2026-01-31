# business logic - separation of concerns from activity_bp (HTTP)

from extensions import db
from models import ActivityLog
from activity_retention import prune_activity_log

# log activity
def log_activity(action, entity_type, entity_id=None, metadata=None):
    if not action or not entity_type:
        return # raise ValueError could work here 
    
    try:
        activity = ActivityLog(
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            metadata=metadata
        )
        db.session.add(activity)
        db.session.commit()

        # Prune old activities automatically - POST is called 
        from services.activity_retention import prune_activity_log
        prune_activity_log()

        raise activity
    
    except Exception as e:
        db.session.rollback()
        print(f"Failed to log activity: {e}")
        return None
