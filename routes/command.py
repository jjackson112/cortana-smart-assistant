from flask import Blueprint, request, jsonify

command_bp = Blueprint("/command", __name__, url_prefix='/api')

@command_bp.route("/api/command", methods=["POST"])
def handle_command():
    data = request.get_json()

    if not data or "command" not in data:
        return jsonify({"error": "No command provided"}), 400

    user_command = data["command"]

    # Simulate Cortana response
    response = f"Cortana processed: {user_command}"

    # Return it as JSON
    return jsonify({"response": response})