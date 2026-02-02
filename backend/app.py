# routes are registered here

from flask import Flask
from extensions import db
from routes.status import status_bp
from routes.health import health_bp
from routes.contacts import contacts_bp
from routes.inventory import inventory_bp
from routes.schedule import schedule_bp
from routes.todo import todo_bp
from services.activity import activity_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cortana.db"
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

    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)