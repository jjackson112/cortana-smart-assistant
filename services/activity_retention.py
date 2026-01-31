# does cron or scheduled jobs, run db migrations or seed data from command line, or provide a CLI interface for Cortana without the server starting
# activity log maintenance - no user interaction, low risk, scales with usage and defines log structure
# Load → prune → save → report - data lifecycle policy

from activity_log import load_activities, save_activities

MAX_ENTRIES = 1000

def prune_activity_log(max_entries=MAX_ENTRIES):
    activities = load_activities() # get list of activity dicts

    if len(activities) <= max_entries:
        return 0
    
    delete_activities = len(activities) - max_entries
    activities = activities[delete_activities:]

    save_activities(activities)

    return delete_activities

    