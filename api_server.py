from flask import Flask
from flask_restful import Api
import api_calls as ac
from client import ClientList
from invoice import InvoiceList, Invoice

app = Flask(__name__)
app.secret_key = 'evolveu'
api = Api(app)


# api.add_resource(Client, '/item/<string:name>')
api.add_resource(ClientList, '/clients')
api.add_resource(InvoiceList, '/invoices')
api.add_resource(Invoice, '/invoice/<int:client_id>')


# @app.route('/clients')
# def api_getAllClients():
#     # Get all clients
#     return ac.getAllClients()

@app.route('/client/<int:id>')
def getClient(id):
    # Serve specific client
    return ac.getClient(id)  # json object

# /sales
# /invoices

# POSTs
# /invoice

@app.route('/')
def index():
    # Serve first component
    return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

