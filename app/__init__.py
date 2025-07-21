from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')

    # Initialize extensions, blueprints, etc.
    # Example: db.init_app(app)

    return app