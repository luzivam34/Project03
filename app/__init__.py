from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
migrate = Migrate()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')

    # Initialize extensions, blueprints, etc.
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    db.init_app(app)
    migrate.init_app(app, db)
    # Create database tables
    
    with app.app_context():
        from app import models
        db.create_all()
    # Import models to ensure they are registered with SQLAlchemy
    return app