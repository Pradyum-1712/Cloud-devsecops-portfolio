from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "Secure",
        "message": "Cloud DevSecOps Portfolio API is Live",
        "version": "1.1.0",
        "environment": os.getenv("FLASK_ENV", "production")
    })

@app.route('/health')
def health():
    return jsonify({"status": "Healthy"}), 200

if __name__ == '__main__':
    # Running on 0.0.0.0 to allow container networking
    app.run(host='0.0.0.0', port=5000)
