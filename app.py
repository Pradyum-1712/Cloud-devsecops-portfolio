# app/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello! This is my secure DevSecOps application."

if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible outside the container
    app.run(host='0.0.0.0', port=5000)
