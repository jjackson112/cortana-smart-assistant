# each route handles a specific HTTP interaction

from flask import Blueprint

status_bp = Blueprint("status", __name__)

@status.route("/status")
def status():
    return {
        "mode": "idle",
        "last_action": "none"
    }