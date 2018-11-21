from flask import Flask
import api_calls as ac

app = Flask(__name__)


# GETs
# /clients    --- all the clients
@app.route('/clients')
def api_getAllClients():
    # Serve first component
    return ac.getAllClients() # json object

# @app.route('/client/:id')
# def getClient(id):
#     # Serve first component
#     return 'Hello world'

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

