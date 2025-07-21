import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications to save resources
    # Additional configuration variables can be added here
    # Example: DATABASE_URL for database connection string
    # Example: DEBUG for enabling debug mode
    # Example: FLASK_APP for the Flask application entry point
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']  # Convert to boolean
    FLASK_APP = os.environ.get('FLASK_APP', 'run.py')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')  # Default to development environment    
    # Add any other configuration variables as needed
    # Example: ALLOWED_HOSTS for allowed hosts in production
    # Example: API_VERSION for versioning the API
    # Example: JWT_TOKEN_EXPIRATION for JWT token expiration time
    # Example: CACHE_TYPE for caching configuration
    # Example: MAIL_SERVER, MAIL_PORT, etc. for email configuration
    # Example: LOGGING_CONFIG for logging configuration
    # Example: CORS_ALLOWED_ORIGINS for CORS configuration
    # Example: JWT_SECRET_KEY for JWT authentication configuration  
    