# each route handles a specific HTTP interaction
# Blueprint acts as a detachable set of routes so not all end up in app.py
# jsonify returns a dict directly in Flask - valid json data as HTTP

from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/api/health")
def health():
    return jsonify(status="online")