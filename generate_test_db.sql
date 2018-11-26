DROP TABLE clients;
DROP TABLE invoices;
DROP TABLE items;

-- --------------------------------------------
-- Create the tables (Clients, Invoices, Items)
-- --------------------------------------------
CREATE TABLE IF NOT EXISTS clients
(
    id      serial NOT NULL,
    name    varchar(100) NOT NULL,
    CONSTRAINT clients_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS invoices
(
    id          serial NOT NULL,
    date        date,
    location    varchar(100) NOT NULL,
    client_id   integer,
    total       money,
    gst         money,
    CONSTRAINT invoices_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS items
(
    id          serial NOT NULL,
    name        varchar(100),
    invoice_id  integer,
    price       money,
    qty         smallint,
    gst         money,
    CONSTRAINT items_pkey PRIMARY KEY (id)
);


-- Populate table clients
INSERT INTO clients (name) values('John Doe');
INSERT INTO clients (name) values('Jane Doe');
INSERT INTO clients (name) values('Next Client');
INSERT INTO clients (name) values('Previous Client');
INSERT INTO clients (name) values('Super Client');

-- Populate table invoices
INSERT INTO invoices (date, location, client_id, total, gst) values('2018-11-03', 'Calgary', 1, 103.98, 5.05);
INSERT INTO invoices (date, location, client_id, total, gst) values('2018-11-07', 'Ottawa', 2, 54.67, 2.61);
INSERT INTO invoices (date, location, client_id, total, gst) values('2018-11-07', 'Calgary', 1, 22.01, 1.00);
INSERT INTO invoices (date, location, client_id, total, gst) values('2018-11-08', 'Vancouver', 3, 50.00, 2.50);
INSERT INTO invoices (date, location, client_id, total, gst) values('2018-11-08', 'Calgary', 4, 60.00, 3.00);

-- Populate items table
INSERT INTO items (name, invoice_id, price, qty, gst) values('Shoe Size 8', 1, 50, 1, 2.50);
INSERT INTO items (name, invoice_id, price, qty, gst) values('Jacket Size XL', 1, 53.98, 1, 2.50);
INSERT INTO items (name, invoice_id, price, qty, gst) values('Pants brown', 2, 54.67, 1, 2.61);
INSERT INTO items (name, invoice_id, price, qty, gst) values('Skirt dashed', 3, 5.00, 3, 0.25);
INSERT INTO items (name, invoice_id, price, qty, gst) values('Blouse ugly', 3, 7.01, 1, 0.25);
INSERT INTO items (name, invoice_id, price, qty, gst) values('Tomato', 4, 10.00, 1, 0.50);
INSERT INTO items (name, invoice_id, price, qty, gst) values('Pasta', 4, 10.00, 1, 0.50);
INSERT INTO items (name, invoice_id, price, qty, gst) values('Onion', 4, 10.00, 1, 0.50);
INSERT INTO items (name, invoice_id, price, qty, gst) values('Pizza', 4, 10.00, 1, 0.50);
INSERT INTO items (name, invoice_id, price, qty, gst) values('Ice Cream', 4, 10.00, 1, 0.50);
INSERT INTO items (name, invoice_id, price, qty, gst) values('Potatos', 5, 10.00, 6, 0.50);

-- Grant permissions to user postgres. To be able to 'see' data in pgadmin4 (not sure if applies to all).
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;

