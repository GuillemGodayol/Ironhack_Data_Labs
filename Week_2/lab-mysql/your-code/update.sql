-- This file is to update elements in the tables --

UPDATE Customers
SET email = 'ppicasso@gmail.com'
WHERE Name = 'Pablo Picasso'
;

UPDATE Customers
SET email = 'lincoln@us.gov'
WHERE Name = 'Abraham Lincoln'
;

UPDATE Customers
SET email = 'hello@napoleon.me'
WHERE Name = 'Napoleón Bonaparte'
;

UPDATE Salespersons
SET store = 'Miami'
WHERE Name = 'Paige Turner'
;