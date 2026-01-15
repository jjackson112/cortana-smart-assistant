# routes are registered here

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from routes.status import status_bp
from routes.health import health_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cortana.db"
db = SQLAlchemy(app)

app.register_blueprint(status_bp)
app.register_blueprint(health_bp)

@app.route("/")
def home():
    return "Cortana is running"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)