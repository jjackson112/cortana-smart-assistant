from flask import Blueprint, request
from utils.response import success, error_response
from assistant_core import to_do_list_mode

assistant_bp = Blueprint("assistant", __name__, url_prefix="/api")

@assistant_bp.route("/assistant", methods=["POST"])
def assistant_command():
    if request.method == "GET":
        return {"status": "assistant route is alive"}
    data = request.get_json()
    if not data:
        return error_response("Invalid JSON", 400)
    
    input_text = data.get("command")
    state = data.get("state")

    print("TESTING")
    result = to_do_list_mode(input_text=input_text, state=state)
    return success(result), 200