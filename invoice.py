from flask_restful import request, Resource
from db import Db

class Invoice(Resource):
    def __init__(self):
        self.db = Db()

    def post(self, client_id):
        # 1. insert new invoice with value zero
        # 2. insert all items, add them up
        # 3. update invoice total & gst values
        # 4. return
        
        # get the data passed in the post
        req_data = request.get_json()
       
        # insert an invoice with $0 owing
        sql = f"INSERT INTO invoices (date, location, client_id, total, gst) values(current_date, 'Calgary', {client_id}, 0, 0) RETURNING id;"
        result_id = self.db.query(sql)
        
        if result_id:
            print("Invoice {result_id} was created.")
        else:
            print("Could not create empty invoice.")

        # insert post data into items table

        return result_id, 201
        
        """ 
                for item in data['items']:
                    query = "INSERT INTO items (name, invoice_id, price, qty, gst) " \
                            "values(%s, %s, %s, %s, %s);"
                    cur.execute(query, (item["item"], invoice_id, item['price'], item['qty'], item['gst']))

                query = "UPDATE invoices Inv " \
                        "SET total = sum_items.subtot, gst = sum_items.subgst " \
                        "FROM (SELECT invoice_id, SUM(price * qty) AS subtot, sum(gst * qty) AS subgst " \
                        "      FROM items " \
                        "      GROUP BY invoice_id) AS sum_items " \
                        "WHERE Inv.id = sum_items.invoice_id " \
                        "  AND Inv.id = %s";
                cur.execute(query, (invoice_id,))
        except:
            return {"message": "An error ocurred inserting the item."}, 500  # internal server error

        """

class InvoiceList(Resource):
    def __init__(self):
        self.db = Db()

    def get(self):
        sql = "SELECT invoices.id, clients.name, invoices.total " \
              "FROM invoices INNER JOIN clients ON invoices.client_id = clients.id;"
        result = self.db.query(sql)
        return result, 200
