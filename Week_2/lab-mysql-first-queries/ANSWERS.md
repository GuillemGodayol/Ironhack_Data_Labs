![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | My first queries

Please, connect to the Data Bootcamp Google Database using the credentials provided in class. Choose the database called *appleStore* (NOT *appleStore2*!). Use the *data* table to query the data about Apple Store Apps and answer the following questions:

**1. Which are the different genres?**
  Games
  Productivity
  Weather
  Shopping
  Reference
  Finance
  Music
  Travel
  Social Networking
  Sports
  Business
  Health & Fitness
  Entertainment
  Photo & Video
  Navigation
  Education
  Lifestyle
  Food & Drink
  News
  Book
  Medical
  Catalogs

**2. Which is the genre with more apps rated?**
Games is the genre with more apps, with 3400 apps.

**3. Which is the genre with more apps?**
Games is the genre with more apps, with 3862 apps.

**4. Which is the one with less?**
Catalogs is the genre with less apps, with 10 apps.

**5. Take the 10 apps most rated.**
Facebook	2974676
Instagram	2161558
Clash of Clans	2130805
Temple Run	1724546
Pandora - Music & Radio	1126879
Pinterest	1061624
Bible	985920
Candy Crush Saga	961794
Spotify Music	878563
Angry Birds	824451

**6. Take the 10 apps best rated by users.**
:) Sudoku +	5
King of Dragon Pass	5
TurboScan™ Pro - document & receipt scanner: scan multiple pages and photos to PDF	5
Plants vs. Zombies	5
Learn to Speak Spanish Fast With MosaLingua	5
Plants vs. Zombies HD	5
The Photographer's Ephemeris	5
▻Sudoku +	5
Flashlight Ⓞ	5
Infinity Blade	5

**7. Take a look on the data you retrieved in the question 5. Give some insights.**
There is no surprise on having two Social Networks in the first positions, as well as have some well-known games at the top10.
The surprise could be to see the Bible in position #7 with almost 1M ratings.

**8. Take a look on the data you retrieved in the question 6. Give some insights.**
There is a mixture of games, and Productivity apps.
Some of the apps are "repeated", such as Plants vs Zombies and Sudoku +

**9. Now compare the data from questions 5 and 6. What do you see?**
Be the mostly rated app doesn't mean to be the top rated app.
Could be that an app with no much ratings is in top of the table for the most rated apps, if all of this ratings are 5.
So, we can say that the most number of ratings we have, the most chances to get a wider range of ratings.

**10. How could you take the top 3 regarding the user ratings but also the number of votes?**
We can select the columns user_rating and rating_count_tot. First we order by user_rating, and then by the rating_count_tot
Head Soccer	5	481564
Plants vs. Zombies	5	426463
Sniper 3D Assassin: Shoot to Kill Gun Game	5	386521

**11. Does people care about the price?** Do some queries, comment why are you doing them and the results you retrieve. What is your conclusion?
CONCLUSION
As seen in the previous queries, people mostly cares about price. That doesn't mean people uses or rates only free apps, but a high percentage are under 2$. A free app or an app at a low price grants you to reach more users. We don't have information about in-app payments, but regarding the information at our hands, it could be a good option to give the app for free or at a low price and then get more revenue through in-app payments.

## Deliverables
You need to submit a `.sql` file that includes the queries used to answer the questions above, as well as an `.md` file including your answers.
