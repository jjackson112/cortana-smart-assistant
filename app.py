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
    mode = db.Column(db.String(50), nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    job = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "mode": self.mode,
            "name": self.name,
            "phone": self.phone,
            "job": self.job,
            "date_added": self.date_added.isoformat()
        }

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(50), nullable=False, index=True)
    category = db.Column(db.String(100), nullable=False, index=True)
    key = db.Column(db.String(200), nullable=False, index=True)
    value = db.Column(db.String(200), nullable=False, index=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "mode": self.mode,
            "category": self.category,
            "key": self.key,
            "value": self.value,
            "date_added": self.date_added.isoformat()
        }

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    updated_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "mode": self.mode,
            "type": self.type,
            "description": self.description,
            "date": self.date,
            "time": self.time,
            "date_added": self.date_added.isoformat(),
            "updated_time": self.updated_time.isoformat()
        }

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.String(50), nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "mode": self.mode,
            "name": self.name,
            "completed": self.completed
        }


app.register_blueprint(status_bp)
app.register_blueprint(health_bp)

@app.route("/")
def home():
    return "Cortana is running"


if __name__ == "__main__":
    app.run(debug=True)