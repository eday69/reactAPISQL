from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv

from client import ClientList, Client
from invoice import InvoiceList, Invoice

app = Flask(__name__)
app.secret_key = 'evolveu'
api = Api(app)
CORS(app)

# load the environment variables from .env file
load_dotenv()

# client routes
api.add_resource(ClientList, '/clients')
api.add_resource(Client, '/client/<int:id>')

# invoice routes
api.add_resource(InvoiceList, '/invoices')
api.add_resource(Invoice, '/invoice/<int:client_id>')

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
