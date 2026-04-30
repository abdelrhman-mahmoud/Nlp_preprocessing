"""Flask application entry point."""
from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from api import api_bp
from utils.logger import app_logger
from utils.exceptions import NLPException


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Register blueprints
    app.register_blueprint(api_bp, url_prefix="/api")

    # Global error handler
    @app.errorhandler(NLPException)
    def handle_nlp_exception(e):
        return jsonify(e.to_dict()), e.status_code

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Endpoint not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500

    @app.route("/")
    def index():
        return jsonify({
            "app":      "NLP Preprocessing API",
            "version":  "1.0.0",
            "endpoints": [
                "GET  /api/health",
                "POST /api/detect-language",
                "POST /api/detect-dialect",
                "GET  /api/functions/<en|ar>",
                "POST /api/preprocess",
                "POST /api/preprocess/smart",
            ],
        })

    app_logger.info("✅ Flask app initialized")
    return app


if __name__ == "__main__":
    app = create_app()
    app_logger.info(f"🚀 Running on http://{Config.HOST}:{Config.PORT}")
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)