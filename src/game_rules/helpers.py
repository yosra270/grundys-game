from dotenv import load_dotenv
from os import environ, path

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

MAX = int(environ.get('MAX')) # Player is the user.
MIN = int(environ.get('MIN')) # Player is the computer.

def grundys_split(number) :
    ''' 
    Function to divide a number to two unequal strictly positive numbers
    '''

    possible_couples = []
    for i in range(1,number//2+1):
        for j in range(i,number):
            if i+j == number and i!=j:
                possible_couples.append([i,j])
    return possible_couples


def ask_for_coins_number():
    return input("How many coins are in the initial heap ? : ")

def ask_for_first_player():    
    print("\nWho plays first ? :\n")
    print("\t1/ You")
    print("\t2/ The program\n") 

    first_turn_player = int(input("_ : "))
    return MAX if (first_turn_player == 1) else MIN


def prompt_action(turn_state, player):
    print("\n", "You" if player == MAX else "Computer", " : ", turn_state)

def prompt_who_won(stuck_player):
    if stuck_player == MIN :
        print("You Won ! Congrats <3")
    else:
        print("You lost :( Sorryy <3")
