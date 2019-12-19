
# 1. Which are the different genres?

select distinct prime_genre 
from data;

# 2. Which is the genre with more apps rated?

select prime_genre, count(*)
from data
where rating_count_tot != 0
group by prime_genre
order by count(*) desc;

# 3. Which is the genre with more apps?

select prime_genre, count(*)
from data
group by prime_genre
order by count(*) desc;

# 4. Which is the one with less?

select prime_genre, count(*)
from data
group by prime_genre
order by count(*);

# 5. Take the 10 apps most rated.

select track_name, rating_count_tot
from data
order by rating_count_tot desc
limit 10;

# 6. Take the 10 apps best rated by users.

select track_name, user_rating
from data
order by user_rating desc
limit 10;

# 10. How could you take the top 3 regarding the user ratings but also the number of votes?

select track_name, user_rating, rating_count_tot
from data
order by user_rating desc, rating_count_tot desc
limit 3;

# 11. Does people care about the price?** Do some queries, comment why are you doing them and the results you retrieve. What is your conclusion?

#Query1: Let's check the price for 10 best rated apps. This will give us a first idea on whether people cares about price or not

select track_name, user_rating, price
from data
order by user_rating desc
limit 10;

# 8 out of 10 best rated apps are non-free. That could indicate that people doesn't care about price and do prefer high quality although it may mean to pay for the app.

#Query2: Let's check the price for 10 most rated apps. We don't know if the previous apps have much ratings or not

select track_name, rating_count_tot, price
from data
order by rating_count_tot desc
limit 10;

# All of the top10 apps in terms of number of ratings are free! So... Maybe that indicates that people cares about price, and the free apps are more used than the non-free apps.

#Query3: Let's check the price for top 10 considering rating and number of rates. We will have a better idea on the relation between price, rating and number of rates.

select track_name, user_rating, rating_count_tot, price
from data
order by user_rating desc, rating_count_tot desc
limit 10;

# 60% of best rated apps with more ratings are free. Other 40% are less than 2$. That may confirm that people cares about price.

#Query4: Let's check how many apps are for each price, so we can see if people downloads apps in function of its price or not 

select price, count(*)
from data
group by price
order by count(*) desc
;

# At a first glance, it seems to be a high difference between free apps (4056) and non-free apps (728 at 0.99), but... sure?

#Query5: Let's check how many apps are non-free

select count(*)
from data
where price != 0
;

# There is a difference, but not so huge as it appeared before: 4.056 free apps vs 3.141 non-free apps. Total 7.197 apps.

#Query6: Let's check how many apps are free or "cheap".

select count(*)
from data
where price <= 1.99
;

# 5.405 apps out of 7.197 (75%) are have a price under 2$

# CONCLUSION
# As seen in the previous queries, people mostly cares about price. That doesn't mean people uses or rates only free apps, but a high percentage are under 2$. A free app or an app at a low price grants you to reach more users. We don't have information about in-app payments, but regarding the information at our hands, it could be a good option to give the app for free or at a low price and then get more revenue through in-app payments.