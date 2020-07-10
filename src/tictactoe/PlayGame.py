#################################  
# File: Play Game               #
# Program in: Tic tac toe game  #
# Main program: MainProgram     #
#                               #
# By: Robert Rebnor             #
#                               #
#################################

from random import randint

import DisplayGame as DisplayGame
import SolveGame as SolveGame

"""
SolutionDict = {'Across the top': ['A1', 'B1', 'C1'],
                'Across the middle': ['A2', 'B2', 'C2'],
                'Across the bottom': ['A3', 'B3', 'C3'],
                'Down the left side': ['A1', 'A2', 'A3'],
                'Down the middle': ['B1', 'B2', 'B3'],
                'Down the right side': ['C1', 'C2', 'C3'],
                'Left down diagonal': ['A1', 'B2', 'C3'],
                'Left up diagonal': ['A3', 'B2', 'C3']
            }
"""


def WhoGoesFirst():
    """Choses which player that starts at random
    """
    if randint(0,1) == 1:
        return 'X'
    else: 
        return 'O'


class PlayGame(DisplayGame.DisplayGame, ):

    def __init__(self):
        super().__init__()

    def Play(self):
        print('')
        print('Let us play Tic Tac Toe.')
        DisplayGame.DisplayGame.DisplayBoard(self)
        self.turn = turn = WhoGoesFirst()
        self.count = 0   
        self.boardDict = boardDict = DisplayGame.grid_values_StartingBoard(self.grid, self.boxes)
        
        for i in range(10):
            print('')
            if i == 0:
                print('Player ' + turn + ' start. Choose your starting box.')
            else:
                print("It's your turn " + turn + ". Please select your move.")

            move = input().capitalize()

            if boardDict[move] == ' ':
                boardDict[move] = turn
                self.count += 1
                DisplayGame.display(self.boxes, self.rows, self.cols, boardDict)
            else:
                print("That place is already filled.\nPlease select another move.")
                continue
            
            # After every successful move, we must check if someone has won - PUT THIS IN OWN CLASS
            gameWon = self.gameWon = None
            SolveGame.SolveGame.Solver(self)

            if gameWon == "done":
                break 
           
            # If the game is not over, we must change player to move
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X' 