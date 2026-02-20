from flask import Blueprint, request, jsonify
from assistant_core import handle_command

# transport logic - extract JSON + pass it to handle_command() in assistant_core.py (FSM)
assistant_bp = Blueprint("assistant", __name__, url_prefix="/api") 

@assistant_bp.route("/assistant", methods=["POST"]) 

def assistant_command(): 
    data = request.get_json() 
    if not data: 
        return jsonify("Invalid JSON", 400) 
    
    input_text = data.get("command")
    state = data.get("state") 
    
    result = handle_command(input_text=input_text, state=state) 
    return jsonify(result), 200