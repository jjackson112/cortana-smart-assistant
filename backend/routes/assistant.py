from flask import Blueprint, request
from modules.to_do_list import ToDo
from utils import success, error_response
from assistant_core import to_do_list_mode

todo = ToDo()
assistant_bp = Blueprint("assistant", __name__, url_prefix="api/assistant")

@assistant_bp.route("/", methods=["POST"])
def assistant_command():
    data = request.get_json()
    if not data:
        return error_response(400)
    
    input_text = data.get("command")
    state = data.get("state")

    result = to_do_list_mode(todo, input_text=input_text, state=state)
    return success(result)