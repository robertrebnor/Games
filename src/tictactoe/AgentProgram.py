#################################  
# File: Agent program           #
# Program in: Tic tac toe game  #
# Main program: MainProgram     #
#                               #
# By: Robert Rebnor             #
#                               #
#################################

import copy


import Moves as Moves



   def CopyBoard(self, OriginalBoard):
        self.CopyBoard = copy.deepcopy(OriginalBoard)
        if self.CopyBoard == OriginalBoard:
            return True
        else:
            return False


class AgentProgram(Moves.NextMoves):

    def __init__(self):
        super().__init__()

    def NextMove(self):
        
        # Test if it can win in the next move
        # Test if it needs to block an win in the next move
        # test if it needs to block a fork in the next move
        # Test if it can move to a corner in the next move
        # test if it can move to a side in the next move

        # start with a corner if it is first?
        # what about the middle?


#SearchTree