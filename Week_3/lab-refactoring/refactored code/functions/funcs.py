# in this file I will define all the functions to be called on the main file.
import random
import sys
import re

# When defining a function, I insert a brief explanation on what it does:

# A function to ask the number of soldiers
def num_of_soldiers(asking_question):
    while True:
        input_string = input(asking_question)
        if re.match('^[1-9]$', input_string) is not None:
            return int(input_string)
        print('Please insert a number from 1 to 9')

# A function to check the number or fices to use by DEFENSIVE:
def check_def_dices(soldiers_number):
    """
    This function checks if the input of the number of dices for defensive Army is a correct value.
    Input: a digit
    Output: the number of defensive dices

    Note 1: Defensive dices are limited to 2.
    Note 2: If there is just one defensive soldier, the function returns directly 1 dice without asking the player.
    """
    asking_question = 'How many DICES do you want to use to DEFEND the new territory?'
    limited = 'The number of attacking dices is limited to'
    not_digit = 'Please insert a number'

    if soldiers_number == 1:
        return 1
    else:
        while True:
            input_string = input(asking_question)
            if re.match('^[1-2]$', input_string) is not None:
                return int(input_string)
            print('Please insert a number from 1 to 2')

# A function to check the number of dices to use by ATTACKING:
def check_att_dices(soldiers_number):
    """
    This function checks if the input of the number of dices for attacking Army is a correct value.
    Input: a digit
    Output: the number of attacking dices

    Note 1: Defensive dices are limited to 2 if there are 2 soldiers. Otherwise is limited to 3.
    Note 2: If there is just one attacking soldier, there is no possibility to attack.
    """
    asking_question = 'How many DICES do you want to use to ATTACK the new territory?'
    limited = 'The number of attacking dices is limited to'
    not_digit = 'Please insert a number'


    if soldiers_number == 2:
        while True:
            input_string = input(asking_question)
            if re.match('^[1-2]$', input_string) is not None:
                return int(input_string)
            print('Please insert a number from 1 to 2')
    else:
        while True:
            input_string = input(asking_question)
            if re.match('^[1-3]$', input_string) is not None:
                return int(input_string)
            print('Please insert a number from 1 to 3')

# A function to generate random dice rolls.
def roll_dices(num_of_dices):
    """
    This function generates as random dice rolls as needed according to the number of dices.
    Input: a digit (number of dices, either defensive or attacking)
    Output: a list of random numbers from 1 to 6 (dice roll)

    Example:
    Input: 2 (Defensive dices)
    Output: [3, 1]
    """
    return [random.randint(1,6) for i in range(num_of_dices)]

# A function to remove the max from a list, in order to compare 2nd max dice rolls
def remove_max(rolls_list):
    try:
        rolls_list.remove(max(rolls_list))
    except ValueError:
        pass
    return rolls_list

# A function to compare the dice rolls and set the loses for each team
def comparing_rolls(def_rolls, att_rolls):
    def_loses = 0
    att_loses = 0
    while len(def_rolls) > 0 and len(att_rolls) > 0:
        if max(att_rolls) > max(def_rolls):
            def_loses += 1
        else:
            att_loses += 1
        att_rolls = remove_max(att_rolls) # applying of previously defined function remove_max
        def_rolls = remove_max(def_rolls) # applying of previously defined function remove_max
    return(def_loses, att_loses)

# A function for the 'Game Over' print
def game_over(defenders, attackers):
    print('\n')
    if defenders == 0:
        print('\033[1;30m'+'GAME OVER. The region is conquered, Attackers WIN!')
    elif attackers == 1:
        print('\033[1;34m'+'GAME OVER. The region is save, Defenders WIN!')