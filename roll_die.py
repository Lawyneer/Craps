'''
roll_die.py - function to roll n number of dice and return the sum.

Inputs:
    num_die - number of dice to be rolled

Outputs:
    total - sum of n dice rolled

Note:
    If the RNG is not seeded in a function/script that calls
    roll_die, then seed the RNG inside by uncommenting 
    random.see() below
'''

# Define function
def roll_die (num_die):
    
    # Import needed packages
    import random # needed for the RNG

    # Initialize variables
    die = [] # list to hold value for each die rolled
    # random.seed() # seed RNG with current system time    

    # for loop to roll each die
    for i in range(num_die):
        die.append(random.randint(1,6)) # roll ith die
    # end for

    # sum the dice and return the value
    total = sum(die)
#    print(total)   # used during testing/debugging
#    print(die)     # used during testing/debugging
    return total

# end function
