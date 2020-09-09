'''
keep_rolling.py - function that returns an indication of winning or losing
                   when a point is established in a craps game

Inputs:
     point - point shooter rolled

Outputs:
    win - indicateion of winning or losing: 1 = win, -1 = lose

Notes:
    Comment out the print statements in the if, elif, else for large
    simulations.  The are included here to allow the user to actually
    simulate playing craps
'''

# Define function
def keep_rolling(point):
    
    # Import needed modules
    import random           # needed for the RNG
    import roll_die as roll # import the function to roll dice
    import time             # needed to pause after rollind die for effect

    # Shooter rolls die
    new_roll = roll.roll_die(2) # craps used two dice

    # Determine if shooter won or lost
    if (new_roll == point): # shooter wins
        win = 1             # set win
        print("Shooter rolled a", new_roll,"to win\n") # prints win to screen
        # Comment out print statement for large simulations

    elif (new_roll == 7): # shooter lost
        win = -1            # set win
        print("Shooter crapped out with a", new_roll,"\n")
    else: # neither point or crapping out
        print("Shooter rolled:", new_roll,"\n")
        delay = random.randint(1,5)
        time.sleep(delay)
        win = keep_rolling(point)
    # end if, elif, else
    
    return win

# end function
