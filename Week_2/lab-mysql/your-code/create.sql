-- In this file I will create the tables for the database. 

-- Table 1. CARS
-- I create the table with ID with autoincrement (that forces the ID to be the Primary Key) because of the excercise.
-- If I would create the table by myself, I wouldn't set an ID column and would use VIN as a Primary Key.

CREATE TABLE CARS (
	ID int AUTO_INCREMENT,
	VIN varchar(30) Not Null,
	Manufacturer varchar(15) Not Null,
	Model varchar(15) Not Null,
	Year YEAR,
	Color tinytext,
	PRIMARY KEY (ID)
	)
;

-- Table 2. CUSTOMERS
-- I create the table with ID with autoincrement (that forces the ID to be the Primary Key) because of the excercise.
-- If I would create the table by myself, I wouldn't set an ID column and would use Cust_ID (NIF/CIF in Spain) as a Primary Key.

CREATE TABLE CUSTOMERS (
	ID int AUTO_INCREMENT,
	Cust_ID varchar(20) Not Null,
	Name varchar(30) Not Null,
	PhoneNum varchar(15) Not Null,
	email varchar(30),
	address varchar(50) Not Null,
	city tinytext Not Null,
	state tinytext Not Null,
	country tinytext Not Null,
	postal_code varchar(15) Not Null,
	PRIMARY KEY (ID)
	)
;


-- Table 3. SALES PERSONS
-- If I needed to create this table from 0, I would include phone number and/or email.

CREATE TABLE SALESPERSONS (
	ID int AUTO_INCREMENT,
	Staff_ID varchar(20) Not Null,
	Name varchar(30) Not Null,
	store tinytext Not Null,
	PRIMARY KEY (ID)
	)
;

-- Table 4. INVOICES
-- I create the table with ID with autoincrement (that forces the ID to be the Primary Key) because of the excercise.
-- If I would create the table by myself, I wouldn't set an ID column and would use InvoiceNum as a Primary Key.

CREATE TABLE INVOICES (
	ID int AUTO_INCREMENT,
	InvoiceNum varchar(20) Not Null,
	Date Date Not Null,
	Car int Not Null,
	Customer int Not Null,
	Sales_Person int Not Null,
	PRIMARY KEY (ID),
	FOREIGN KEY (Car) REFERENCES CARS(ID),
	FOREIGN KEY (Customer) REFERENCES CUSTOMERS(ID),
	FOREIGN KEY (Sales_Person) REFERENCES SALESPERSONS(ID)
	)
;