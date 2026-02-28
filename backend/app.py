# routes are registered here

import os
from flask import Flask
from .extensions import db
from flask_cors import CORS
from .routes.status import status_bp
from .routes.health import health_bp
from .routes.contacts import contacts_bp
from .routes.inventory import inventory_bp
from .routes.schedule import schedule_bp
from .routes.todo import todo_bp
from .routes.assistant import assistant_bp
from .services.activity import activity_bp

def create_app():
    app = Flask(__name__)
    CORS(app, origins=[
        "http://localhost:3000",
        os.getenv("FRONTEND_URL", "*")
    ])
    
    # Database configuration
    db_url = os.getenv("DATABASE_URL", "sqlite:///cortana.db")
    # Fix Render's postgres URL for SQLAlchemy
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    # bind extensions
    db.init_app(app)

    app.register_blueprint(status_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(contacts_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(todo_bp)
    app.register_blueprint(activity_bp)
    app.register_blueprint(assistant_bp)

    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))