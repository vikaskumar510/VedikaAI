from flask import Flask, jsonify
import random
import os

# Constants for better performance
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the coffee file a police report? It got mugged!",
    "What do you call fake spaghetti? An impasta!",
    "Why was the math book sad? Because it had too many problems!",
]

def create_app():
    """Application factory pattern for better initialization and testing."""
    app = Flask(__name__)

    # Environment-based configuration
    app.config['ENV'] = os.getenv('FLASK_ENV', 'production')
    app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

    @app.route('/joke', methods=['GET'])
    def random_joke():
        """Return a random joke with caching headers for improved performance."""
        try:
            joke = random.choice(JOKES)
            response = jsonify({'joke': joke})
            # Add cache control headers to improve performance for repeated requests
            response.headers['Cache-Control'] = 'public, max-age=60'
            return response
        except Exception as e:
            # Proper error handling to prevent performance degradation
            return jsonify({'error': 'Unable to retrieve joke', 'message': str(e)}), 500

    @app.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint for monitoring."""
        return jsonify({'status': 'healthy'}), 200

    return app

# Create the app instance
app = create_app()

if __name__ == '__main__':
    # Use environment variables to control debug mode
    # Debug mode disabled by default for production performance
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('FLASK_PORT', '5000'))
    host = os.getenv('FLASK_HOST', '0.0.0.0')

    app.run(host=host, port=port, debug=debug_mode)