from math import inf
from dotenv import load_dotenv
from os import environ

from game_rules.game_rules import Game, game_configuration
from game_rules.helpers import prompt_action, prompt_who_won


# Find .env file
load_dotenv()

MAX = int(environ.get('MAX')) # Player is the user.
MIN = int(environ.get('MIN')) # Player is the computer.


nbr_developed_nodes = 0
nbr_prunned_brunches = 0

def minimaxab_decision(turn):    
    actions = turn.get_possible_actions()
    global nbr_developed_nodes
    nbr_developed_nodes = nbr_developed_nodes + 1
    
    # All possibles actions with their corresponding minimax values
    possibles_minimaxab_choices = { tuple(action):minimaxab(Game(action,-turn.player), -inf, +inf) for action in actions} 
    
    # Choose best action depending on the player.
    if(turn.player == MAX):
        return Game(list(max(possibles_minimaxab_choices)), MIN)
    else:
        return Game(list(min(possibles_minimaxab_choices)), MAX)
    
    
def minimaxab(turn,alpha,beta):
    actions = turn.get_possible_actions()
    global nbr_prunned_brunches
    global nbr_developed_nodes
    nbr_developed_nodes = nbr_developed_nodes + 1
    
    if turn.player == MAX:
        if actions == []: # Terminal node.
            return turn.get_utility()
        
        max_value = -inf
        for action in actions:
            max_value = max(max_value, minimaxab(Game(action,MIN),alpha,beta))
            if max_value >= beta:
                nbr_prunned_brunches = nbr_prunned_brunches + (len(actions) -(actions.index(action) + 1)) # Number of prunned brunches is the remaining unexplored subnodes.
                return max_value
            alpha = max(alpha, max_value)
        return max_value

    else:
        if actions == []: # Terminal node.
            return turn.get_utility()
        
        min_value = +inf
        for action in actions:
            min_value = min(min_value, minimaxab(Game(action,MAX),alpha,beta))
            if min_value <= alpha:
                nbr_prunned_brunches = nbr_prunned_brunches + (len(actions) -(actions.index(action) + 1))
                return min_value
            beta = min(beta, min_value)
        return min_value

def play_ab():
    global nbr_developed_nodes
    global nbr_prunned_brunches
    
    initial_turn = game_configuration()
    turn = initial_turn
    while(not turn.is_game_over()): # Game is over when all heaps are of size 1 or 2
        turn = turn.get_next_action(minimaxab_decision)
        prompt_action(turn.state, -turn.player)
    
    stuck_player = turn.player # Player stuck in the last round is the one who loses the game
    
    print()    
    
    prompt_who_won(stuck_player)
    
    print("\nNumber of developed nodes: " , nbr_developed_nodes)
    
    print("Number of elagage: " , nbr_prunned_brunches)