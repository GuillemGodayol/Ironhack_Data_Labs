# CHALLENGE 1

# STEP 1
SELECT ta.au_id, ta.title_id, t.advance * ta.royaltyper / 100 as 'advance', t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as sales_royalty

from titleauthor ta
JOIN titles t ON t.title_id = ta.title_id
JOIN sales s ON s.title_id = ta.title_id
;

# STEP 2

SELECT au_id, title_id, advance, sum(sales_royalty) as 'royalties'
from (SELECT ta.au_id, ta.title_id, t.advance * ta.royaltyper / 100 as 'advance', t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as sales_royalty
		from titleauthor ta
		JOIN titles t ON t.title_id = ta.title_id
		JOIN sales s ON s.title_id = ta.title_id) as royalty_per_sale
GROUP BY au_id, title_id
;

# STEP 3

SELECT au_id, sum(advance + royalties) as 'total_profit'
	from (SELECT au_id, title_id, advance, sum(sales_royalty) as 'royalties'
			from (SELECT ta.au_id, ta.title_id, t.advance * ta.royaltyper / 100 as 'advance', t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as sales_royalty
					from titleauthor ta
					JOIN titles t ON t.title_id = ta.title_id
					JOIN sales s ON s.title_id = ta.title_id) as royalty_per_sale
		GROUP BY au_id, title_id) as royalty_per_title
GROUP BY au_id
ORDER BY total_profit desc
LIMIT 3
;

## ------------------ ##

# CHALLENGE 2

# STEP 1
CREATE TEMPORARY TABLE TEMP1 
SELECT ta.au_id, ta.title_id, t.advance * ta.royaltyper / 100 as 'advance', t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 as sales_royalty
from titleauthor ta
JOIN titles t ON t.title_id = ta.title_id
JOIN sales s ON s.title_id = ta.title_id
;

#STEP 2
CREATE TEMPORARY TABLE TEMP2
SELECT au_id, title_id, advance, sum(sales_royalty) as 'royalties'
from TEMP1
GROUP BY au_id, title_id, advance
;

#STEP 3
SELECT au_id, sum(advance + royalties) as 'total_profit'
from TEMP2
GROUP BY au_id
ORDER BY total_profit desc
LIMIT 3
;

## ----------------  ##

# CHALLENGE 3

CREATE TABLE most_profiting_autors
SELECT au_id, sum(advance + royalties) as 'total_profit'
from TEMP2
GROUP BY au_id
ORDER BY total_profit desc
;