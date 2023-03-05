
DROP DATABASE IF EXISTS GLO2005_TP;

CREATE DATABASE IF NOT EXISTS GLO2005_TP;
USE GLO2005_TP;

/*------------------------------------------------ Tables des objets: ------------------------------------------------*/

CREATE TABLE IF NOT EXISTS humans (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    username VARCHAR(100),
    password VARCHAR(100),
    PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS admins (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES humans(id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS vendors (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    description VARCHAR(500),
    address VARCHAR(100),
    phone_number VARCHAR(100) CHECK ( phone_number REGEXP '^[0-9]{3}-[0-9]{3}-[0-9]{4}$' ),
    email VARCHAR(100) CHECK ( email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$' ),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES humans(id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS customers (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    address VARCHAR(100),
    phone_number VARCHAR(100) CHECK ( phone_number REGEXP '^[0-9]{3}-[0-9]{3}-[0-9]{4}$' ),
    email VARCHAR(100) CHECK ( email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$' ),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES humans(id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS products (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    description VARCHAR(100),
    price FLOAT,
    category_id INT,
    PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS carts (
    id INT NOT NULL AUTO_INCREMENT,
    total_cost FLOAT,
    PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS payment_systems (
    id INT NOT NULL AUTO_INCREMENT,
    payment_type VARCHAR(100),
    PRIMARY KEY (id));

/*----------------------------------------------- Tables des relations: ----------------------------------------------*/

CREATE TABLE IF NOT EXISTS vendors_adds_products (
    vendor_id INT,
    product_id INT,
    PRIMARY KEY (vendor_id, product_id),
    FOREIGN KEY (vendor_id) REFERENCES vendors(id) ON DELETE CASCADE ON UPDATE CASCADE,
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

CREATE TABLE IF NOT EXISTS carts_pay_with_payment_systems (
    cart_id INT,
    payment_system_id INT,
    PRIMARY KEY (cart_id, payment_system_id),
    FOREIGN KEY (cart_id) REFERENCES carts(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (payment_system_id) REFERENCES payment_systems(id) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS customer_use_payment_system (
    customer_id INT,
    payment_system_id INT,
    PRIMARY KEY (customer_id, payment_system_id),
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (payment_system_id) REFERENCES payment_systems(id) ON DELETE CASCADE ON UPDATE CASCADE);

/*------------------------------ INSÉRER CI-DESSOUS LE CODE À SUPPRIMER AVANT LA REMISE ------------------------------*/

DROP DATABASE IF EXISTS GLO2005_TP;
