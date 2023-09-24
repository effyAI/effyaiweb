# cors_config.py
from flask_cors import CORS
def configure_cors(app):
    # Configure CORS to allow requests from your Vercel domain
    CORS(app, resources={r"/api/*": {"origins": "https://www.bandhanfutureready.com/"}})
