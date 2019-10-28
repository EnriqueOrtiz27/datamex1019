CREATE DATABASE lab_mysql;
USE lab_mysql;

CREATE TABLE cars (counter INT, car_id INT, manufacturer VARCHAR(20), year INT, color VARCHAR(15), price INT);

CREATE TABLE salespersons (staff_ID INT, staff_name VARCHAR(30), store VARCHAR(20));

CREATE TABLE customers (customer_counter INT, customer_ID INT, customer_name VARCHAR(20), customer_phone INT, customer_email VARCHAR(40), customer_address VARCHAR(90), customer_city VARCHAR(45), customer_country VARCHAR(40), customer_manufacturer VARCHAR(40), customer_car_id INT);

CREATE TABLE invoices (invoice_date DATE, invoice_car_id INT, invoice_manufacturer VARCHAR(40), invoice_customer_id INT, invoice_STAFF_id INT);


