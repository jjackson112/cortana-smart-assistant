# routes are registered here

from flask import Flask
from extensions import db
from routes.status import status_bp
from routes.health import health_bp
from services.activity import activity_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cortana.db"

    app.register_blueprint(status_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(activity_bp)

    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)