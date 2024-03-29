
DROP DATABASE IF EXISTS GLO2005_TP;

CREATE DATABASE GLO2005_TP;
USE GLO2005_TP;

/*------------------------------------------------ Tables des objets: ------------------------------------------------*/

CREATE TABLE IF NOT EXISTS humans (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    username VARCHAR(100),
    password VARCHAR(100),
    PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS sellers (
    id INT UNIQUE NOT NULL,
    name VARCHAR(100),
    description VARCHAR(500),
    address VARCHAR(100),
    phone_number VARCHAR(100), CONSTRAINT seller_phone_number_invalid CHECK ( phone_number REGEXP '^[0-9]{3}-[0-9]{3}-[0-9]{4}$' ),
    email VARCHAR(100), CONSTRAINT seller_email_invalid CHECK ( email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$' ),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES humans(id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS customers (
    id INT UNIQUE NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    address VARCHAR(100),
    phone_number VARCHAR(100), CONSTRAINT customer_phone_number_invalid CHECK ( phone_number REGEXP '^[0-9]{3}-[0-9]{3}-[0-9]{4}$' ),
    email VARCHAR(100), CONSTRAINT customer_email_invalid CHECK ( email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$' ),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES humans(id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS products (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    size VARCHAR(100),
    image_src VARCHAR(200),
    price FLOAT,
    category VARCHAR(100),
    PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS carts (
    id INT NOT NULL AUTO_INCREMENT,
    total_cost FLOAT,
    PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS payment_systems (
    id INT NOT NULL AUTO_INCREMENT,
    payment_type VARCHAR(100),
    number VARCHAR(100),
    expiration_date VARCHAR(100),
    cvv VARCHAR(100),
    PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS invoices (
    id INT NOT NULL AUTO_INCREMENT,
    customer_id INT,
    total_cost FLOAT,
    date DATE,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE ON UPDATE CASCADE);

/*----------------------------------------------- Tables des relations: ----------------------------------------------*/

CREATE TABLE IF NOT EXISTS sellers_adds_products (
    seller_id INT,
    product_id INT,
    PRIMARY KEY (seller_id, product_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS customers_own_carts (
    customer_id INT,
    cart_id INT,
    PRIMARY KEY (customer_id, cart_id),
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (cart_id) REFERENCES carts(id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS carts_contains_products (
    cart_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (cart_id, product_id),
    FOREIGN KEY (cart_id) REFERENCES carts(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS customer_own_payment_system (
    customer_id INT,
    payment_system_id INT,
    PRIMARY KEY (customer_id),
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (payment_system_id) REFERENCES payment_systems(id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS invoice_contains_products (
    invoice_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (invoice_id, product_id),
    FOREIGN KEY (invoice_id) REFERENCES invoices(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE ON UPDATE CASCADE);

/*----------------------------------------------------- Triggers -----------------------------------------------------*/

CREATE TRIGGER update_total_cost_after_insert
    AFTER INSERT ON carts_contains_products
    FOR EACH ROW
    BEGIN
        UPDATE carts
        SET total_cost = total_cost + (SELECT price FROM products WHERE id = NEW.product_id) * NEW.quantity
        WHERE id = NEW.cart_id;
    END;

CREATE TRIGGER update_total_cost_after_delete
    AFTER DELETE ON carts_contains_products
    FOR EACH ROW
    BEGIN
        UPDATE carts
        SET total_cost = total_cost - (SELECT price FROM products WHERE id = OLD.product_id) * OLD.quantity
        WHERE id = OLD.cart_id;
    END;

CREATE TRIGGER update_total_cost_after_update
    AFTER UPDATE ON carts_contains_products
    FOR EACH ROW
    BEGIN
        UPDATE carts
        SET total_cost = total_cost - (SELECT price FROM products WHERE id = OLD.product_id) * OLD.quantity
        WHERE id = OLD.cart_id;
        UPDATE carts
        SET total_cost = total_cost + (SELECT price FROM products WHERE id = NEW.product_id) * NEW.quantity
        WHERE id = NEW.cart_id;
    END;

CREATE TRIGGER update_total_cost_after_insert_invoice
    AFTER INSERT ON invoice_contains_products
    FOR EACH ROW
    BEGIN
        UPDATE invoices
        SET total_cost = total_cost + (SELECT price FROM products WHERE id = NEW.product_id) * NEW.quantity
        WHERE id = NEW.invoice_id;
    END;

CREATE TRIGGER create_cart_for_customer
    AFTER INSERT ON customers
    FOR EACH ROW
    BEGIN
        INSERT INTO carts (total_cost) VALUES (0);
        INSERT INTO customers_own_carts (customer_id, cart_id) VALUES (NEW.id, LAST_INSERT_ID());
    END;

CREATE TRIGGER delete_last_payment_system
    BEFORE UPDATE ON customer_own_payment_system
    FOR EACH ROW
    BEGIN
        DELETE FROM payment_systems WHERE id = OLD.payment_system_id;
    END;

/*---------------------------------------------------- Indexation ----------------------------------------------------*/

CREATE INDEX invoice_id ON invoice_contains_products (invoice_id);

CREATE INDEX cart_id ON carts_contains_products (cart_id);

CREATE INDEX seller_id ON sellers_adds_products (seller_id);
