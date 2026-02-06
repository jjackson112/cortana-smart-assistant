# accept user input + sends it to Cortana's brain (main.py) then returns the reply 
from flask import Blueprint, request
from utils.response import error_response

cortana_bp = Blueprint("command", __name__, url_prefix='/api')

@cortana_bp.route("/command", methods=["POST"])
def handle_command():
    data = request.get_json()
    if not data:
        return error_response("Missing command text", 400)
    
    