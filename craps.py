'''
craps.py - function that returns the amount won or lost from a single game of craps.

Inputs:
    bet - an amount bet on either the pass or don't pass line
    line - 1 for the pass line and 2 for the don't pass line

Outputs:
    winnings - the amount of money a player won/lost.  See note 2.

Notes:
    1.  I tried to order the various if/elif statements in the highest probabilty
        that they would occur so that the ones with the lowest probability of 
        occurring would be checked last.  In other words, I don't want to check
        for a 12 first when it is the least likey thing to be rolled (besides a two).

    2.  Right now the code is set for a player winning even money on a pass or don't
        pass line bet.  Working othe code to include taking/laying odds.

    3.  Comment out the print statements for large simulations.  The are included 
        here to allow the user to actually simulate playing craps.

'''
# Define function
def craps( bet, line):

    # Import needed modules
    import random               # needed for the RNG
    import roll_die as roll     # function to roll dice
    import keep_rolling as kr   # function to keep rolling when a point is set

    # Establish point
    point = roll.roll_die(2)            # roll dice
    print("The point is: ", point,"\n") # print point

    # Determine outcome of game
    if (point == 7 or point == 11): # shooter rolls 7 or 11 on come out roll
        if (line == 1):     # pass line win
            winnings = bet  # player wins bet
            print("Pass line shooter wins with a ",point,"\n") # print winner
        else: # don't pass line loser
            winnings = -bet # player loses bet
            print("Don't pass line shooter loses with a ",point,"\n") # print loser
        # end if, else

    elif (point == 6 or point == 8): # shooter rolls 6 or 8 on come out roll

        outcome = kr.keep_rolling(point) # shooter keeps rolling to determine outcome
        
        if (outcome == 1): # shooter won
            if (line == 1): # pass line win
                winnings = bet  # player wins bet
            else: # don't pass line lose
                winnings = -bet # player loses bet
            # end if, else

        else: # shooter lost
            if (line == 1): # pass line lose
                winnings = -bet # player loses bet
            else: # don't pass line win
                winnings = bet  # player wins bet
            # end if, else

        # end if, else

    elif (point == 5 or point == 9): # shooter rolls 5 or 9 or come out roll

        outcome = kr.keep_rolling(point) # shooter keeps rolling to determine outcome

        if (outcome == 1): # shooter won
            if (line == 1): # pass line win
                winnings = bet  # player wins bet
            else: # don't pass line lose
                winnings = -bet # player loses bet
            # end if, else

        else: # shooter lost
            if (line == 1): # pass line lose
                winnings = -bet # player loses bet
            else: # don't pass line win
                winnings = bet  # player wins bet
            # end if, else

        # end if, else

    elif (point == 4 or point == 10): # shooter rolls 4 or 10 on come out roll
        
        outcome = kr.keep_rolling(point) # shooter keeps rolling to determine outcome

        if (outcome == 1): # shooter won
            if (line == 1): # pass line win
                winnings = bet  # player wins bet
            else: # pass line lose
                winnings = -bet # player loses bet
            # end if, else
            
        else: # shooter lost
            if (line == 1): # pass line lose
                winnings = -bet # player loses bet
            else: # pass line win
                winnings = bet  # player wins bet
            # end if, else

        # end if, else

    elif (point == 2 or point == 3): # shooter rolls 2 or 3 on come out roll
        if (line == 1): # pass line lose
            winnings = -bet # player loses bet
            print("Pass line shooter loses with a ", point, "\n") # print lose
        else: # don't pass line win
            winnings = bet  # player wins bet
            print("Don't pass line shooter loses with a ", point, "\n") # print win
        # end if, else
    
    else: # shooter rolled a 12 on come out roll
        if (line == 1): # pass line lose
            winnings = -bet # player loses bet
            print("Pass line shooter loses with a ", point, "\n") # print lose
        else: # don't pass line push
            winnings = 0    # player niether wins or loses bet
            print("Don't pass line shooter pushes with a ", point, "\n") # print push
        # end if, else

    return winnings # return winnings

# end function
