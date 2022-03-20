from helpers import grundys_split, ask_for_coins_number, ask_for_first_player
import sys
from dotenv import load_dotenv
from os import environ, path

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

MAX = int(environ.get('MAX')) # Player is the user.
MIN = int(environ.get('MIN')) # Player is the computer.

class Game:
    def __init__(self,state,player = MAX):
        self.state = state # A state is defined with the heaps resulting from previous actions.
        self.player = player


    def get_possible_actions(self):
        ''' 
        This function computes all possible actions that a player can choose to play at a particular state of the game.

        An action = choose a heap and split it into two unequal heaps.
        So this function will :
            1. Look for all heaps that can be splitted into two unequal heaps (<=> heaps of size > 2).
            2. Choose a heap at a time and :
                2.1. Compute all its possible splits (e.g. We can split a heap containing 7 coins in three different ways 7 => [1, 6] or [2, 5] or [3, 4]).
                2.2. For each splitting possbility :
                     a. Replace the old heap with the new two heaps in the current state.
                     b. Return the result as an action.
        '''

        actions = []
        state = self.state   

        # Searching for all heaps that can be splitted into two unequal heaps (heaps of size > 2).
        for index in range(len(state)) :
            heap = state[index]
            if (heap > 2):
                # Computing all possible splits of a heap.
                all_possible_splits = grundys_split(heap)
                for two_heaps in all_possible_splits:
                    new_state = state.copy()
                    # Replace old heap with the new splitted heaps.
                    new_state.pop(index)
                    new_state.insert(index, two_heaps[0])
                    new_state.insert(index + 1, two_heaps[1])

                    actions.append(new_state)
        return actions


    def get_next_action(self, algorithm):
        '''
        This function returns the action chosen by players in the current turn.

        When it's the computer's turn to play : 
            The computer will choose the best action among all possible actions depending on the decision rule used (minimax or alpha-beta prunning in our case).
        
        When it's the user's turn to play :
            The user will enter the new sequence which should be checked against the rules of the game.
        '''
        if self.player == MAX : # Player is the user
            old_state = self.state
            sequence = input("What is the new sequence ? : ")
            new_state = list(map(int, sequence.split(" "))) # New state

            self.check_rules(new_state) # User should split only one heap at a time into two two heaps of different size
            self.state = new_state

            self.player = MIN # Now it is the turn of the computer to play.
            return self
        else: # Player is the program (MIN)
            return algorithm(self)


    def check_rules(self, new_state):
        ''' User should split only one heap at a time into two heaps of different non-zero sizes. '''

        old_state = self.state
        if len(old_state) != len(new_state)-1:
            sys.exit("Illegal move : you can split one heap at a time")
        
        if 0 in new_state:
            sys.exit("Illegal move : heaps should be of size > 0.")
            
        first_mismatch = next( (index_first_mismatch, old_heap, new_first_heap) for index_first_mismatch, (old_heap, new_first_heap) in enumerate(zip(old_state, new_state)) if old_heap!=new_first_heap )
        if (first_mismatch[1] == first_mismatch[2]*2): # size of one of the new heaps = half size the original before the split
            sys.exit("Illegal move : heaps should not be of same size")
        
        if(sum(old_state) != sum(new_state)):
            sys.exit("Illegal move : the split is not write; please rectify the numbers of jetons in the new heaps")
    

    def get_utility(self) : 
        # Make sure the game has ended.
        if not self.is_game_over():
            sys.exit("Game is not over yet !")

        # Compute the utility.
        if self.player == MAX: #MAX is stuck -> loss
            return -1
        return 1

    def is_game_over(self):
        # All heaps are of size 1 or 2.
        return all(heap <= 2 for heap in self.state)
    


def game_configuration():
    '''
    Initialize a game with :
        * Number of coins in the initial heap.
        * Who starts the game (User or Computer).
    '''
    # Number of coins in the initial heap.
    coins_number = int(ask_for_coins_number())

    # Who starts the game : the user or the computer.   
    first_turn_player = ask_for_first_player()
    
    return Game([coins_number], first_turn_player)




