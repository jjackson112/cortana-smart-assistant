# routes are registered here

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from routes.status import status_bp
from routes.health import health_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cortana.db"
db = SQLAlchemy(app)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    job = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(100), nullable=False, index=True)
    key = db.Column(db.String(200), nullable=False, index=True)
    value = db.Column(db.String(200), nullable=False, index=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

app.register_blueprint(status_bp)
app.register_blueprint(health_bp)

@app.route("/")
def home():
    return "Cortana is running"


if __name__ == "__main__":
    app.run(debug=True)