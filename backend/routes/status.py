# each route handles a specific HTTP interaction

from flask import Blueprint, jsonify

status_bp = Blueprint("status", __name__, url_prefix='/status')

@status_bp.route("/api/status", methods=["GET"])
def get_status():
    return jsonify(
        mode ="idle",
        last_action = "none"
    )