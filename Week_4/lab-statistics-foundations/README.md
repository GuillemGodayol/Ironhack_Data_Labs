![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Statistics Foundations
In this lab we are going to put into practice what we learned about the foundations of statistics. You won't need to use Python, just your brain and a little bit of *Markdown*. 

## Your task
Today you'll need to complete the challenges described below.

## Deliverables
You need to submit a markdown file with the solution to the following challenges. You can create a new *.md* file or directly edit the *README.md* to include your solutions.

## Challenges
### Challenge 1
One player rolls two dices. Describe the measurable space and the random variable for:
* A. The values that the player obtains.
{(1,1),(1,2)...(1,6),(2,1)...(2,6)...(5,6),(6,6)}
* B. The sum of the values obtained.
(2,3,4,5,6,7,8,9,10,11,12)
* C. The maximum value obtained after rolling both dices. (6,6) = (12)

Describe the following events:
* Case A: Both values are greater than 5.
Both greater than 5 can just be 1 case: P(6,6) = 1/6*1/6 = 1/36
* Case B: The sum of values is even.
(1,1),(1,3),(1,5),(2,1),(2,3),(2,5),(3,1),(3,3),(3,5),(4,2),(4,4),(4,6),(5,1),(5,3),(5,5),(6,2),(6,4),(6,6) - P(sum is even) = 18/36 = 1/2
* Case C: The maximum is the value of both rolls.
P = 0. We can't have the maximum as the value of a roll.

### Challenge 2
One player picks two cards from a poker deck. Describe the measurable space and the random variable for:
* A. The number of figures he picks.
He can pick 3 figures (J, Q, K) of 4 types, so the measurable space is 12 figures.
* B. The sum of card values. Consider that the value of figures is 10 and the value of aces is 15. 
The measurable space for 2 picks will go from 4 (2 cards with 2) to 30 (2 aces)
* C. The number of hearts or spades he picks.
There's 13 cards of each type, so the measurable space for hearts or spades picked will go from 0 to 26.

Describe the following events:
* Case A: The number of figures in the cards the player picked is two.
There are 12 figures out of 52 cards. so the P(2 figures) = 12/52 * 11/51 = 132 / 2.652 = 11/221
* Case B: The sum of card values is 17.
To sum 17 there are some options: Ace + 2, figure + 7, 10 + 7 and 9 + 8. So there is a total amount of 16 + 48 + 16 + 16 = 96 posible combinations out of 2704. P(sum17) = 96/2704 = 6/169 
* Case C: The value of both cards is less than 8.
Cards can go from 2 to 5 (there's no 1), but second card depends on the first one.  
P(<8) = [P(2)*P(2,3,4,5)] + [P(3)*P(2,3,4)] + ... + [P(5)*P(2)] 

### Challenge 3
Two players roll a dice. Describe the measurable space and the random variable for:
* A. The score of player A. 
{1,2,3,4,5,6}
* B. The greatest score.
{6}
* C. The earnings of player A if the game rules state that:  
"The player with the greatest score gets a coin from the other player.".
{-1,0,1}
* D. The earnings of player A if the game rules state that:  
"The player with the greatest score gets as many coins as the difference between the score of player A and player B.". 
{-5, -4, -3 ... 0 ... 4, 5}

Describe the following events:
* Case A: The score of player A is 2.
P(A=2) = 1/6
* Case B: The greatest score is lower or equal than 2.
P(<=2) = P(A=(1,2))*P(B=(1,2)) = 2/6 * 2/6 = 1/9
* Case C: Considering the case where the winner gets as many coins as the difference between scores (D), describe: 
  * Player A wins at least 4 coins.
  P(A>4coins) = P(A=5)*P(B=1) + P(A=6)*P(B=(1,2)) = 1/6*1/6 + 1/6*2/6 = 1/36 + 2/36 = 1/12
  * Player A loses more than 2 coins.
  P(A<-2coins) = P(A=3)*P(B=6) + P(A=2)*P(B=(5,6)) + P(A=1)*P(B=(4,5,6))= 1/6*(1/6 + 2/6 + 3/6) = 1/6 
  * Player A neither wins nor loses coins.
  P(A=0) = P(A=B) = 1/6

## Bonus challenges
### Bonus Challenge 1
Three players take balls from a box. Inside that box there are red, blue, green and black balls. The players can take three balls at mosts with the following rules:

* If the ball is blue, they can take another ball.
* If the ball is green, they get one point and they can take another ball.
* If the ball is red, they can’t take another ball.
* If the ball is black, they lose one point and they can’t take another ball.

Describe the measurable space and the random variable for:
* A. Player A wins. Do not consider ties as a win.
* B. Player A and B get the same points.
* C. All players get 0 points.

### Bonus Challenge 2
Consider the situation of bonus challenge 1 but now with four players. Does anything change in your solutions? What are the changes in each case?

### Bonus Challenge 3
One player takes three balls from a box. Inside the box there are 5 balls: two of them are black and the other three are white. 

Describe the measurable space and the random variable for:
* A. The number of white balls if every time we take a ball we keep it.
* B. The number of white balls if every time we take a ball we put it back again into the box.
* C. The number of black balls if every time we take a ball we keep it.
* D. The number of black balls if every time we take a ball we put it back into the box.