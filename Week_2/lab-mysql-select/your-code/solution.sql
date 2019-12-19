-- Challenge 1 - Who Have Published What At Where?
-- we need to join 4 tables to get all the columns we should show. And for each join we need to specify the connection.

select authors.au_id as Author_ID,
	au_lname as Last_Name,
	au_fname as First_Name,
	title as Title,
	pub_name as Publisher
from authors
	join titleauthor on authors.au_id = titleauthor.au_id
	join titles on titleauthor.title_id = titles.title_id
	join publishers on titles.pub_id = publishers.pub_id
where au_ord = 1
-- we select just au_ord = 1 because some titles have more than 1 author and then the titler and publisher appear repeated.
;

-- Challenge 2 - Who Have Published How Many At Where?
-- we take the previous query and change title for count(title) as we want to get the total. We group by author and Publisher and order them descending by title_count.
select authors.au_id as Author_ID,
	au_lname as Last_Name,
	au_fname as First_Name,
	count(title) as Title_Count,
	pub_name as Publisher
from authors
	join titleauthor on authors.au_id = titleauthor.au_id
	join titles on titleauthor.title_id = titles.title_id
	join publishers on titles.pub_id = publishers.pub_id
group by authors.au_id, Publisher
order by Title_Count desc
;

-- Challenge 3 - Best Selling Authors
-- first we join the tables to get all the neede columns. In this case, we will sum the 'ytd_sales' column to get the total of titles solds

Select authors.au_id as Author_ID,
	au_lname as Last_Name,
	au_fname as First_Name,
	sum(ytd_sales) as Total
from authors
	join titleauthor on authors.au_id = titleauthor.au_id
	join titles on titleauthor.title_id = titles.title_id
	group by Author_ID
order by Total desc
limit 3
;

-- Challenge 4 - Best Selling Authors Ranking
-- we need to include those authors with no sales, so we need 'Left joins'

Select a.au_id as Author_ID,
	au_lname as Last_Name,
	au_fname as First_Name,
	sum(ytd_sales) as Total
from authors as a
	left join titleauthor as ta on a.au_id = ta.au_id
	left join titles as t on ta.title_id = t.title_id
group by Author_ID
order by Total desc
;