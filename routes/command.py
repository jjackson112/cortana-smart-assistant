# does cron or scheduled jobs, run db migrations or seed data from command line, or provide a CLI interface for Cortana without the server starting
# activity log maintenance - no user interaction, low risk, scales with usage and defines log structure

def prune_activity_log(max_entries=1000):
    activities = load_activities()

    if len(activities) <= max_entries:
        return 0
    