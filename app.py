# routes are registered here

from flask import Flask
from routes.status import status_bp

app = Flask("__name__")
app.register_blueprint(status_bp)

@app.route("/")
def home():
    return "Cortana is running"

if __name__ == "__main__":
    app.run(debug=True)