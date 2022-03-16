from game import Game, possible_actions, utility, game_configuration, game_over, MAX, MIN, next_action, prompt_action, who_won

nbr_developed_nodes =0

def minimax_decision(tour):    
    actions = possible_actions(tour)
    global nbr_developed_nodes
    nbr_developed_nodes = nbr_developed_nodes + 1
    
    # all possibles tours with their corresponding minimax values
    possibles_minimax_choices = { tuple(action):minimax(Game(action,-tour.player)) for action in actions} 
    
    if(tour.player == MAX):
        return Game(list(max(possibles_minimax_choices)), MIN)
    else:
        return Game(list(min(possibles_minimax_choices)), MAX)
    
def minimax(tour):
    actions = possible_actions(tour)
    global nbr_developed_nodes
    nbr_developed_nodes = nbr_developed_nodes + 1
    
    if tour.player == MAX:
        if actions == []:
            return utility(tour)
        min_values = [minimax(Game(action,MIN)) for action in actions]
        return max(min_values)

    else:
        if actions == []:
            return utility(tour)
        max_values = [minimax(Game(action,MAX)) for action in actions]
        return min(max_values)


def play():
    global nbr_developed_nodes
    
    initial_tour = game_configuration()
    tour = initial_tour
    while(not game_over(tour)): # Game is over when all heaps are of size 1 or 2
        tour = next_action(tour, minimax_decision)
        prompt_action(tour.state, -tour.player)
    
    stuck_player = tour.player # Player stuck in the last round is the one who loses the game
    
    print()
    
    who_won(stuck_player)
    
    print("\nNumber of developed nodes: " , nbr_developed_nodes)
