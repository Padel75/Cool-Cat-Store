CREATE DATABASE IF NOT EXISTS GLO2005_TP;
USE GLO2005_TP;

CREATE TABLE IF NOT EXISTS humans (id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY (id)); /* Est ce que le nom et le password iraient pas dans cette table?*/

/* Est ce que la notion de privilège serait ici pertinente?*/
CREATE TABLE IF NOT EXISTS admins (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(100), password VARCHAR(100),
                                   PRIMARY KEY (id), FOREIGN KEY (id) REFERENCES humans(id));
/*Creer contrainte pour addresse?*/
CREATE TABLE IF NOT EXISTS vendors (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(100), password VARCHAR(100), username VARCHAR(100), description VARCHAR(100), address VARCHAR(100),
                                    PRIMARY KEY (id), FOREIGN KEY (id) REFERENCES humans(id));

/*Creer domaine pour email et pour phone_number*/
CREATE TABLE IF NOT EXISTS customers (id INT NOT NULL AUTO_INCREMENT, first_name VARCHAR(100), last_name VARCHAR(100), username VARCHAR(100), password VARCHAR(100), address VARCHAR(100), phone_number VARCHAR(100), email VARCHAR(100),
                                      PRIMARY KEY (id), FOREIGN KEY (id) REFERENCES humans(id));

CREATE TABLE IF NOT EXISTS products (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(100), description VARCHAR(100), price FLOAT, category_id INT,
                                    PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS carts (id INT NOT NULL AUTO_INCREMENT, total_cost FLOAT,
                                  PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS payment_systems (id INT NOT NULL AUTO_INCREMENT, payment_type VARCHAR(100),
                                            PRIMARY KEY (id));
