from math import inf
from game import Game, possible_actions, utility, game_configuration, game_over, MAX, MIN, next_action, prompt_action, who_won

nbr_developed_nodes = 0
nbr_elagage = 0

def minimaxab_decision(tour):    
    actions = possible_actions(tour)
    global nbr_developed_nodes
    nbr_developed_nodes = nbr_developed_nodes + 1
    
    # all possibles tours with their corresponding minimax values
    possibles_minimaxab_choices = { tuple(action):minimaxab(Game(action,-tour.player), -inf, +inf) for action in actions} 
    
    if(tour.player == MAX):
        return Game(list(max(possibles_minimaxab_choices)), MIN)
    else:
        return Game(list(min(possibles_minimaxab_choices)), MAX)
    
    
def minimaxab(node,alpha,beta):
    actions = possible_actions(node)
    global nbr_elagage
    global nbr_developed_nodes
    nbr_developed_nodes = nbr_developed_nodes + 1
    
    if node.player == MAX:
        if actions == []: # Noeud terminal
            return utility(node)
        
        max_value = -inf
        for action in actions:
            max_value = max(max_value, minimaxab(Game(action,MIN),alpha,beta))
            if max_value >= beta:
                nbr_elagage = nbr_elagage + (len(actions) -(actions.index(action) + 1)) # nbre des branches élaguées est le reste de sous-noeuds non explorés
                return max_value
            alpha = max(alpha, max_value)
        return max_value

    else:
        if actions == []: # Noeud terminal
            return utility(node)
        
        min_value = +inf
        for action in actions:
            min_value = min(min_value, minimaxab(Game(action,MAX),alpha,beta))
            if min_value <= alpha:
                nbr_elagage = nbr_elagage + (len(actions) -(actions.index(action) + 1))
                return min_value
            beta = min(beta, min_value)
        return min_value

def play_ab():
    global nbr_developed_nodes
    global nbr_elagage
    
    initial_tour = game_configuration()
    tour = initial_tour
    while(not game_over(tour)): # Game is over when all heaps are of size 1 or 2
        tour = next_action(tour, minimaxab_decision)
        prompt_action(tour.state, -tour.player)
    
    stuck_player = tour.player # Player stuck in the last round is the one who loses the game
    
    print()    
    
    who_won(stuck_player)
    
    print("\nNumber of developed nodes: " , nbr_developed_nodes)
    
    print("Number of elagage: " , nbr_elagage)