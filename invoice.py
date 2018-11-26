from flask_restful import request, Resource
    # , reqparse
import psycopg2


class Invoice(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('items')
    # parser.add_argument("items", location="json")
    # parser.add_argument("items", type = dict, location="json")
    # parser.add_argument('gst',
    #                     type=float,
    #                     required=True,
    #                     help="GST cannot be blank!"
    #                     )

    def post(self, client_id):
        # 2. insert all items, add them up
        # 3. update invoice total & gst values
        # 4. return

        # 1. insert new invoice with value zero
        query = "INSERT INTO invoices (date, location, client_id, total, gst) " \
                "values(current_date, 'Calgary', %s, 0, 0) RETURNING id;"
        conn = psycopg2.connect('dbname=evolveu')
        cur = conn.cursor()
        try:
            cur.execute(query, (client_id,))
            print('QUERY', client_id, query)
            row = cur.fetchone()
            if row:
                invoice_id = row[0]
                invoice =  {'invoice_id': invoice_id}

                data = request.get_json()

                # print('DATA', data['items'])
                #
                # print('Before for in')
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

        conn.commit()
        cur.close()
        conn.close()
        return invoice, 201  # created


class InvoiceList(Resource):
    def get(self):
        sql = "SELECT invoices.id, clients.name, invoices.total " \
              "FROM invoices INNER JOIN clients ON invoices.client_id = clients.id;"

        conn = psycopg2.connect('dbname=evolveu')
        cur = conn.cursor()
        cur.execute(sql)

        invoices = []
        rows = cur.fetchall()
        for row in rows:
            invoices.append({'id': row[0], 'name': row[1], 'total': row[2]})

        cur.close()
        conn.close()

        return {'invoices': invoices}
