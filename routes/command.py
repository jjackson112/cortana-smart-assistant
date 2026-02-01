from flask import Blueprint, request, jsonify

command_bp = Blueprint("command", __name__, url_prefix='/api')

@command_bp.route("/api/command", methods=["POST"])
def handle_command():
    data = request.json()
    user_command = data.get("command")

    # Simulate Cortana response
    response = f"Cortana processed: {user_command}"

    # Return it as JSON
    return jsonify({"response": response})