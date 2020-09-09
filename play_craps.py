'''
play_craps.py - script to allow a user to play a simple texted based game of craps.

Inputs:
    bet - user input bet amount
    line - user input to select a pass or don't pass line bet
    
Outputs:
    Print if the player wins, loses, pushes, and how much was won/lost.
    Other functions called from within print out rolls as shooter rolls

Notes:
    This has been run and tested on linux and Mac machines.
    
'''

# Import needed packages
import craps as crps    # function to play craps
from os import system, name 

# Initialize variables
bank_roll = 500     # starting bankroll
keep_playing = 1    # termination condition


while(keep_playing == 1 and bank_roll > 0):
    
    # Clear screen from last game
    if(name == 'nt'): # Windows machine
        _ = system('cls')
    else: # linux and Mac machines
        _ = system('clear')
    # end if, else
        
    # Prompt user for a bet
    bet = int(input("Please enter a bet.\n"))
    
    # Make sure bankroll covers bet
    if(bet > bank_roll):
        print("Bet too high.  Max bet is: ",bank_roll,"\n")
        bet = int(input("Please reenter bet.\n"))
    # end if
    
    # Prompt user to line
    line = int(input("Enter 1 for a pass line bet and 2 for a don't pass line bet.\n"))
        
    # Play the game
    win = crps.craps(bet, line)
    
    # Print results
    if(win < 0): # print lose
        print("The shooter lost -$",abs(win),".\n")
    elif(win > 0): # Print win
        print("The shooter won $", win, "\n")
    else: # print push
        print("The shooter pushes")
    # end if, elif, else
    
    # Update bankroll
    bank_roll = bank_roll + win
    print("Current bankroll is: $",bank_roll,"\n")
    
    # Determine if play continues
    if(bank_roll <= 0): # Check if player busted
        print("You're bust.  Please try again.\n")
    else: # prompt user to keep playing
        keep_playing = int(input("Enter 1 to keep playing or 0 to quit.\n"))
        if(keep_playing < 0 or keep_playing > 1):
            print("\nInput error.\n")
            keep_playing = int(input("Enter 1 to keep playing or 0 to quit.\n"))
        # end if
    # end if, else

# end while loop
