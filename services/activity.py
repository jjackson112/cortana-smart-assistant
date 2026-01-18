# how Cortana behaves as not just when data exists with timestamps
# central activity service + exposes records services = business logic
# create a Blueprint - GET
# where will the activity live - memory or persistence? - business logic

from flask import Blueprint
from routes import contacts, inventory, schedule, todo

activity_bp = Blueprint("activity", __name__, url_prefix='/api/activity')

# each activity for each mode (CRUD) gets its own endpoint - check routes for separate files
# GET requests don't need a request body - no JSON validation or request.get_json()
# No CRUD, models, db, or validation - better organization