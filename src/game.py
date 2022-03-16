from twoparts import twoParts
import sys

MAX = 1
MIN = -1

class Game:
    def __init__(self,state,player = MAX):
        self.state = state
        self.player = player


def possible_actions(node):
    actions = []
    state = node.state   
    for index in range(len(state)) :
        pile = state[index]
        if (pile>2):
            two_parts = twoParts(pile)  # 7 => [[1, 6], [2, 5], [3, 4]]
            for couple in two_parts:
                new_state = state.copy()
                new_state.pop(index) # remove element from list
                new_state.insert(index, couple[0])
                new_state.insert(index + 1, couple[1])
                actions.append(new_state)
    return actions
#print(possible_actions(Game([1,4,4,2,1],MAX)))

def utility(node):
    if node.player == MAX: #MAX is stuck -> loss
        return -1
    return 1


def game_configuration():
    # Nbre de jetons de la pile initiale
    nbre_jetons = int(input("Give the initial number of jetons : "))
    # Le premier joueur : le programme ou l'utilisateur
    print("\nWho plays first :\n")
    print("\t1/ You")
    print("\t2/ The program\n")    

    first_round_player = int(input("_ : "))
    player = MAX if (first_round_player == 1) else MIN
    
    return Game([nbre_jetons], player)

def game_over(tour):
    # all heaps are of size 1 or 2
    return all(heap <= 2 for heap in tour.state)

def check_rules(old_state, new_state):
    if len(old_state) != len(new_state)-1:
        sys.exit("Illegal move : you can split one heap at a time")
        
    first_mismatch = next( (index_first_mismatch, old_heap, new_first_heap) for index_first_mismatch, (old_heap, new_first_heap) in enumerate(zip(old_state, new_state)) if old_heap!=new_first_heap )
    if (first_mismatch[1] == first_mismatch[2]*2): # size of one of the new heaps = half size the original before the split
        sys.exit("Illegal move : heaps should not be of same size")
    
    if(sum(old_state) != sum(new_state)):
        sys.exit("Illegal move : the split is not write; please rectify the numbers of jetons in the new heaps")

def next_action(tour, algorithm):
    if tour.player == MAX : # Player is the user
        old_state = tour.state
        sequence = input("Quelle est la nouvelle séquence ? : ")
        tour.state = list(map(int, sequence.split(" "))) # New state
        check_rules(old_state, tour.state) # User should split only one heap at a time into two two heaps of different size
        tour.player = MIN
        return tour
    else: # Player is the program
        return algorithm(tour)

def prompt_action(tour_state, player):
    print("\n", "You" if player == MAX else "Computer", " : ", tour_state)

def who_won(stuck_player):
    if stuck_player == MIN :
        print("You Won ! Congrats <3")
    else:
        print("You lost :( Sorryy <3")