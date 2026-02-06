# accept user input + sends it to Cortana's brain (main.py) then returns the reply 
from flask import Blueprint, request
from utils.response import error_response, success
from main import to_do_list_mode

cortana_bp = Blueprint("command", __name__, url_prefix='/api')

@cortana_bp.route("/command", methods=["POST"])
def handle_command():
    data = request.get_json()
    if not data or "text" not in data:
        return error_response("Missing command text", 400)
    
    result = to_do_list_mode(
        text=data["text"], # otherwise just a string
        state=data.get("state") # frontend owns this
    )

    return success({
        "messages": result["messages"],
        "events": result["state"],
        "events": result.get("events", []) # optional to change UI and not touch routes
    })