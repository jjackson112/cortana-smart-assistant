from flask import Blueprint, request
from modules.to_do_list import ToDo
from utils.response import success, error_response
from assistant_core import to_do_list_mode

todo = ToDo()
assistant_bp = Blueprint("assistant", __name__, url_prefix="/api/assistant")

@assistant_bp.route("", methods=["GET", "POST"])
def assistant_command():
    if request.method == "GET":
        return {"status": "assistant route is alive"}
    data = request.get_json()
    if not data:
        return error_response("Invalid JSON", 400)
    
    input_text = data.get("command")
    state = data.get("state")

    print("TESTING")
    result = to_do_list_mode(todo, input_text=input_text, state=state)
    return success(result), 200

    