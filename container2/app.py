from flask import Flask, request


app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        json = {}
        return json
    else:
        return 'Welcome to the container 2'

        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='6000')