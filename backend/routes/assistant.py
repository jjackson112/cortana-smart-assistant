from flask import Blueprint, request, jsonify
from ..assistant_core import handle_command

# transport logic - extract JSON + pass it to handle_command() in assistant_core.py (FSM)
assistant_bp = Blueprint("assistant", __name__, url_prefix="/api") 

@assistant_bp.route("/assistant", methods=["POST"]) 

def assistant_command(): 
    data = request.get_json(force=True) # force ensures JSON parsing
    print("RAW DATA", data)

    if not data: 
        return jsonify("Invalid JSON", 400) 
    
    input_text = data.get("input_text")
    state = data.get("state") or {"mode": None, "state": None}
    
    result = handle_command(input_text=input_text, state=state) 
    return jsonify({
        "messages": result.get("messages", []),
        "response": result.get("response", []),
        "state": result.get("state", {"mode": None, "state": None})
    }), 200