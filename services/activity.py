# how Cortana behaves as not just when data exists with timestamps
# central activity service + exposes records
# create a Blueprint - GET
# where will the activity live - memory or persistence?

from flask import Blueprint, requests, jsonify

activity_bp = Blueprint("activity", __name__, url_prefix='/api/activity')

# in-memory storage - replace with database later
state = {
    "contacts": [],
    "tasks": [],
    "inventory": [],
    "schedule": []
}

# each activity gets its own endpoint