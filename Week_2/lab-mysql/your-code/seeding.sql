-- This file is to code the queries to seed the tables

-- Table 1: CARS
-- runned --

INSERT INTO CARS (VIN, Manufacturer, Model, Year, Color)
Values('3K096I98581DHSNUP',	'Volkswagen',	'Tiguan',	2019,	'Blue'),
		('ZM8G7BEUQZ97IH46V',	'Peugeot',	'Rifter',	2019,	'Red'),
		('RKXVNNIHLVVZOUB4M',	'Ford',	'Fusion',	2018,	'White'),
		('HKNDGS7CU31E9Z7JW',	'Toyota',	'RAV4',	2018,	'Silver'),
		('DAM41UDN3CHU2WVF6',	'Volvo',	'V60',	2019,	'Gray'),
		('DAM41UDN3CHU2WVF6',	'Volvo',	'V60 Cross Country',	2019,	'Gray')
;

-- Table 2: CUSTOMERS
-- runned --

INSERT INTO CUSTOMERS (Cust_ID, Name, PhoneNum, email, address, city, state, postal_code)
Values (10001,	'Pablo Picasso',	'+34 636 17 63 82',	'-',	'Paseo de la Chopera, 14',	'Madrid',	'Madrid',	'Spain',	28045),
		(20001,	'Abraham Lincoln',	'+1 305 907 7086',	'-',	'120 SW 8th St',	'Miami',	'Florida',	'United States',	33130),
		(30001,	'Napoléon Bonaparte',	'+33 1 79 75 40 00',	'-',	'40 Rue du Colisée',	'Paris',	'Île-de-France',	'France',	75008)
;

-- Table 3: SALESPERSONS
-- runned --

INSERT INTO SALESPERSONS(Staff_ID, name, Store)
Values (00001,	'Petey Cruiser',	'Madrid'),
		(00002,	'Anna Sthesia',	'Barcelona'),
		(00003,	'Paul Molive',	'Berlin'),
		(00004,	'Gail Forcewind',	'Paris'),
		(00005,	'Paige Turner',	'Mimia'),
		(00006,	'Bob Frapples',	'Mexico City'),
		(00007, 'Walter Melon', 'Amsterdam'),
		(00008,	'Shonda Leer',	'São Paulo')
;

-- Table 4: INVOICES
-- runned --

INSERT INTO INVOICES (InvoiceNum, Date, Car, Customer, Sales_person)
Values ('852399038', '2018-08-22',	7,	2,	3),
		('731166526', '2018-12-31',	11,	1,	5),
		('271135104', '2019-01-22',	9,	3,	7)
;