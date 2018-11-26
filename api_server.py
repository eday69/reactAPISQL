from flask import Flask
from dotenv import load_dotenv

import api_calls as ac

# load the environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/clients')
def api_getAllClients():
    return ac.get_all_clients()

@app.route('/client/<int:id>')
def getClient(id):
     return ac.get_client(id)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
