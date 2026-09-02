#app factory 

from flask import Flask 
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.config.Config')  # Load configuration from config.py
    from flask_wtf.csrf import CSRFProtect
    csrf = CSRFProtect(app)  # Enable CSRF protection
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    return app