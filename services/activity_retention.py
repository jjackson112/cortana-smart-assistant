# does cron or scheduled jobs, run db migrations or seed data from command line, or provide a CLI interface for Cortana without the server starting
# activity log maintenance - no user interaction, low risk, scales with usage and defines log structure
# Load → prune → save → report - data lifecycle policy

from extensions import db
from models import ActivityLog

MAX_ENTRIES = 1000

def prune_activity_log(max_entries=MAX_ENTRIES):
    count = ActivityLog.query.count() # get list of activity dicts

    if count <= max_entries:
        return 0
    
    delete_activities = count - max_entries

    old_entries = (
        ActivityLog.query
        .order_by(ActivityLog.timestamp.asc())
        .limit(delete_activities)
        .all()
    )

    for entry in old_entries:
        db.session.delete(entry)

    db.session.commit()
    return delete_activities

    