# Grundy's Game

Using this application, a user can switch turns with the computer playing grundy's game. 

## Rules of the game
Given a heap of size n, two players alternately select a heap and divide it into two unequal heaps. A player loses when he cannot make a legal move because all heaps have size 1 or 2.

## Game theory
When it is the turn of the computer to play, a decision rule will be used to decide which action to choose among all possible actions.

Decision rules implemented are :
    - Minimax.
    - Minimax with alpha-beta prunning.
