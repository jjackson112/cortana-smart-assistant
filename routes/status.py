# each route handles a specific HTTP interaction

from flask import Blueprint, jsonify

status_bp = Blueprint("status", __name__)

@status_bp.route("/status", methods=["GET"])
def get_status():
    return jsonify(
        mode ="idle",
        last_action = "none"
    )