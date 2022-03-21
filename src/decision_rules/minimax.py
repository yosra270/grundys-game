from dotenv import load_dotenv
from os import environ

from game_rules.game_rules import Game, game_configuration
from game_rules.helpers import prompt_action, prompt_who_won


# Find .env file
load_dotenv()

MAX = int(environ.get('MAX')) # Player is the user.
MIN = int(environ.get('MIN')) # Player is the computer.

nbr_developed_nodes =0

def minimax_decision(turn):  
    '''
    This function chooses the best action a player can play based on its minimax value.
    '''  
    actions = turn.get_possible_actions()
    global nbr_developed_nodes
    nbr_developed_nodes = nbr_developed_nodes + 1
    
    # All possibles actions with their corresponding minimax values.
    possibles_minimax_choices = { tuple(action):minimax(Game(action,-turn.player)) for action in actions} 
    
    # Choose best action depending on the player.
    if(turn.player == MAX):
        return Game(list(max(possibles_minimax_choices)), MIN)
    else:
        return Game(list(min(possibles_minimax_choices)), MAX)
    
def minimax(turn):
    actions = turn.get_possible_actions()
    global nbr_developed_nodes
    nbr_developed_nodes = nbr_developed_nodes + 1
    
    if turn.player == MAX:
        if actions == []:
            return turn.get_utility()
        min_values = [minimax(Game(action,MIN)) for action in actions]
        return max(min_values)

    else:
        if actions == []:
            return turn.get_utility()
        max_values = [minimax(Game(action,MAX)) for action in actions]
        return min(max_values)


def play():
    global nbr_developed_nodes
    
    initial_turn = game_configuration()
    turn = initial_turn
    while(not turn.is_game_over()): # Game is over when all heaps are of size 1 or 2.
        turn = turn.get_next_action(minimax_decision)
        prompt_action(turn.state, -turn.player)
    
    stuck_player = turn.player # Player stuck in the last round is the one who loses the game.
    
    print()
    
    prompt_who_won(stuck_player)
    
    print("\nNumber of developed nodes: " , nbr_developed_nodes)
