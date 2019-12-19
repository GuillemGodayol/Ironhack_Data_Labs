from functions import funcs as f

# Phase 1: Asking soldiers
# To get a short game, it is limited to 10. We need integers bigger than 0 to play.
def_soldiers = f.num_of_soldiers("How many soldiers are DEFENDING your territory?")
att_soldiers = f.num_of_soldiers("How many soldiers are ATTACKING from your territory?")

# Phase 2: Asking and checking dices:



# Phase 3: Here is where the round starts.
# There will be a loop until there is a winner.
# The loop will be running while either defending soldiers are bigger than 0, as they can still defend their territory
# and the attacking soldiers are bigger than 1, following the game rules.
while def_soldiers > 0 and att_soldiers > 1:
    print('\n')
    # we start the round with information about the number of soldiers for each team.
    print(f'For the next round, there are {def_soldiers} DEFENSIVE soldiers and {att_soldiers} ATTACKING soldiers')

    # the number of dices to throw are set to 0, then the players will choose how many, if they can.
    def_dices = 0
    att_dices = 0

    # check the number of remaining defending soldiers to decide the number of dices.
    def_dices = f.check_def_dices(def_soldiers)

    # check the number of remaining attacking soldiers to decide the number of dices.
    att_dices = f.check_att_dices(att_soldiers)

    # generating random dice rolls
    def_rolls = f.roll_dices(def_dices)
    print('\n')
    print('The rolls for defending dices in this round are: ', def_rolls)

    att_rolls = f.roll_dices(att_dices)
    print('\n')
    print('The rolls for attacking dices in this round are: ', att_rolls)

    # comparing rolls
    loses = f.comparing_rolls(def_rolls, att_rolls)
    def_soldiers = def_soldiers - loses[0]
    att_soldiers = att_soldiers - loses[1]

    # printing loses
    # A function to print the evolution of the war, the loses of each team, after each battle
    def printing_loses(list):
        defenders = 'Defenders'
        attackers = 'Attackers'
        loose_defenders = f'loose {loses[0]}'
        loose_attackers = f'loose {loses[1]}'
        singular = 'soldier'
        plural = 'soldiers'
        print('\n')
        if list[0] > 1:
            print(defenders, loose_defenders, plural)
        elif list[0] == 1:
            print(defenders, loose_defenders, singular)
        if list[1] > 1:
            print(attackers, loose_attackers, plural)
        elif list[1] == 1:
            print(attackers, loose_attackers, singular)

    printing_loses(loses)
    print('\n')
    print('Round is finished.')

# printing the 'Game Over'
f.game_over(def_soldiers, att_soldiers)