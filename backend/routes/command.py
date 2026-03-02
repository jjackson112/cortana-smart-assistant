from flask import Blueprint, request, jsonify

command_bp = Blueprint("command", __name__, url_prefix='/api')

@command_bp.route("/command", methods=["POST"])
def process_command():
    data = request.get_json()

    if not data or "command" not in data:
        return jsonify({"error": "No command provided"}), 400

    user_command = data["command"]

    # Simulate Cortana response
    response = f"Cortana processed: {user_command}"

    # Return it as JSON
    return jsonify({"response": response})

# React        → sends "5"
# command.py  → interprets "Exit"
# services    → log activity
# React        ← receives "See you next time!"
