from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    import google.generativeai as genai
    genai.configure(api_key="AIzaSyBvTIhZ0ZfUn8-gIAddFchtyx-tvB5YkGY")

    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
