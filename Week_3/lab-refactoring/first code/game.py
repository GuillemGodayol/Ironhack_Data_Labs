#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
import re

# # Defining some functions

# ## Function 'check_def_dices'
# 
# With this function we check or assign the number of dices that will be used for the defending team. If there is just 1 soldier, the player can just use 1 dice. If theres more than 1 soldier, the player can choose to use 1 or 2 dices. 
# 
# In the function, we first check if there is 1 soldier, to assign just 1 dice. If there are more, then we ask the player to choose how many dices he/she wants to use. Then we check if this input is 1 or 2 and assign it into de variable or ask for a new input if the entered number is not valid.

# In[9]:


# a function to check the number of dices to use by DEFENDING.
def check_def_dices(soldiers_number):
    asking_question = 'How many DICES do you want to use to DEFEND the new territory?'
    limited = 'The number of attacking dices is limited to'
    if soldiers_number == 1:
        return 1
    else:
        def_dices = int(input(asking_question))
        while def_dices not in range(1,3):
            print(limited, '2')
            def_dices = int(input(asking_question))
        return def_dices


# ## Function 'check_att_dices'
# 
# With this function we check or assign the number of dices that will be used for the attacking team. If there is just 1 soldier, the attacking team can not play, so we avoided this case.
# 
# If there are two players, the player can choose to use 1 or 2 dices. If theres more than 2 soldiers, the player can choose to use 1, 2 or 3 dices.
# 
# In the function, we first check if there are 2 soldier, to ask the player to choose how many dices he/she wants to use. Then we check if this input is 1 or 2 and assign it into de variable or ask for a new input if the entered number is not valid.
# If there are more than 2 players, we do the same but considering up to 3 dices are valid.

# In[10]:


# a function to check the number of dices to use by ATTACKING:
def check_att_dices(soldiers_number):
    asking_question = 'How many DICES do you want to use to ATTACK the new territory?'
    limited = 'The number of attacking dices is limited to'
    if soldiers_number == 2:
        att_dices = int(input(asking_question))
        while att_dices not in range(1,3):
            print(limited, '2')
            att_dices = int(input(asking_question))
    else:
        att_dices = int(input(asking_question))
        while att_dices not in range(1,4):
            print(limited, '3')
            att_dices = int(input(asking_question))
    return att_dices

# ## Function 'roll_dices'
# 
# For this function we need the number of dices as an input. We will generate a list with the random numbers from 1 to 6 with as many arguments as the numbers of dices we have. 
# 
# It is valid for any team, as we will assign the result in different variables.

# In[11]:


def roll_dices(num_of_dices):
    rolls = []
    while len(rolls) < num_of_dices:
        rolls.append(random.randint(1,6))
    return rolls

# ## Function 'remove_max'
# 
# This function will be used to remove the maximum random roll on the roll dices after each 'combat'. That will allow us to get a new maximum of the newly generated list of rolls.

# In[12]:


def remove_max(rolls_list):
    try:
        rolls_list.remove(max(rolls_list))
    except ValueError:
        pass
    return rolls_list

# ## Function 'comparing_rolls'
# 
# Using this function we will compare the different rolls until we have compared all, and checking the loses for each team.

# In[13]:


def comparing_rolls(def_rolls, att_rolls):
    def_loses = 0
    att_loses = 0
    while len(def_rolls) > 0 and len(att_rolls) > 0:
        if max(att_rolls) > max(def_rolls):
            def_loses += 1
        else:
            att_loses += 1
        att_rolls = remove_max(att_rolls)
        def_rolls = remove_max(def_rolls)
    return(def_loses, att_loses)

# ## Function 'printing_loses'
# 
# For this function we will need the list with 2 arguments returned by the 'comparing_rolls' function, where the first argument represents the defending loses and the second one the attacking loses.
# 
# Depending on that number of loses, we will print the text with the number of loses and the word 'soldier' in singular or plurar accordingly.

# In[14]:


def printing_loses(list):
    defenders = 'Defenders'
    attackers = 'Attackers'
    loose_defenders = f'loose {loses[0]}'
    loose_attackers = f'loose {loses[1]}'
    singular = 'soldier'
    plural = 'soldiers'
    if list[0] > 1:
        print('\n')
        print(defenders, loose_defenders, plural)
    elif list[0] == 1:
        print('\n')
        print(defenders, loose_defenders, singular)
    if list[1] > 1:
        print('\n')
        print(attackers, loose_attackers, plural)
    elif list[1] == 1:
        print('\n')
        print(attackers, loose_attackers, singular)

# ## Function 'game_over'
# 
# This function is just to print the 'GAME OVER' text. If defending soldiers became 0, attackers win. If attackers soldiers became 1, defenders win, as there is one soldier needed for attackers to stay in their territory.

# In[15]:


def game_over(defenders, attackers):
    if defenders == 0:
        print('\n')
        print('\033[1;30m GAME OVER. The region is conquered, Attackers WIN!')
    elif attackers == 1:
        print('\n')
        print('\033[1;34m GAME OVER. The region is save, Defenders WIN!')

# # Here starts the code for the game

# ## Phase 1: Ask for the defending soldiers

# In[16]:


# To get a short game, it is limited to 10. We need integers bigger than 0 to play.

asking_defenders = "How many soldiers are DEFENDING your territory?"
def_soldiers = int(input(asking_defenders))

while def_soldiers not in range(1,11):
    print("The number of soldiers must be between 1 and 10")
    def_soldiers = int(input(asking_defenders))

# ## Phase 2: Ask for attacking soldiers

# In[17]:


# To get a short game, it is limited to 10. The rules of the game say that the attacking soldiers must be at least 2.

asking_attackers = "How many soldiers are ATTACKING your territory?"
att_soldiers = int(input(asking_attackers))
while att_soldiers not in range(2,11):
    print("The number of soldiers must be between 2 and 10")
    att_soldiers = int(input(asking_attackers))

# ## Phase 3: WAR!

# In[18]:


# Here is where the round starts. 
# There will be a loop until there is a winner.
# The loop will be running while either defending soldiers are bigger than 0, as they can still defend their territory
# AND the attacking soldiers are bigger than 1, following the game rules.

while def_soldiers > 0 and att_soldiers > 1:
    print('\n')
    # we start the round with information about the number of soldiers for each team.
    print(f'For the next round, there are {def_soldiers} DEFENSIVE soldiers and {att_soldiers} ATTACKING soldiers')
    
    # the number of dices to throw are set to 0, then the players will choose how many, if they can.
    def_dices = 0
    att_dices = 0

    # check the number of remaining defending soldiers to decide the number of dices.
    def_dices = check_def_dices(def_soldiers)
            
    # check the number of remaining attacking soldiers to decide the number of dices.
    att_dices = check_att_dices(att_soldiers)
    
    # generating random dice rolls
    def_rolls = roll_dices(def_dices)
    print('\n')
    print('The rolls for defending dices in this round are: ', def_rolls)
    
    att_rolls = roll_dices(att_dices)
    print('\n')
    print('The rolls for attacking dices in this round are: ', att_rolls)
    
    # comparing rolls
    loses = comparing_rolls(def_rolls, att_rolls)
    def_soldiers = def_soldiers - loses[0]
    att_soldiers = att_soldiers - loses[1]
    
    # printing loses
    printing_loses(loses)
    print('\n')
    print('Round is finished.')

# ## Phase 4: Game Over!

# In[19]:


# printing the 'Game Over'
game_over(def_soldiers, att_soldiers)
