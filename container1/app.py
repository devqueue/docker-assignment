from flask import Flask, request
import os
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the app'


@app.route('/checksum', methods=['GET', 'POST'])
def checksum():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        json = {}
        if (content_type == 'application/json'):
            json = request.json
            param_exists = json.get('file', False)
        
            if not param_exists:
                json = {
                    "file": "null",
                    "error": "invalid JSON input",
                }
            else:
                if not os.path.exists(f"/data/{param_exists}"):
                    json['error'] = "File not found."
                else:
                    requests.post(url='localhost:6000', json=json)

        return json
    else:
        return 'Send a json via POST'

        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')