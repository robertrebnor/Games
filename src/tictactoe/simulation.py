
### Put this below "PlayWithPlayers" and "AgentPrograms" and above "PlayGame"?

from humans import PlayWithPlayers
from agents import AgentPrograms


import Moves as moves 

class simulation(PlayWithPlayers, AgentPrograms):

    def __init__(self):
        super().__init__()

    def run_through_all():
        #run a complete simulation:
            # there should be 362 880 unique games that can be played, but that is the "theoretical" max number of games
                # count the number games that have equal boards.
                # the 9 first moves have each 8 
            # 9 starting moves
            # run through a win, loss or draw.
                # Save all moves, and the correct order
                # Save the game result
        PossibleMoves = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']

        for firstmove in PossibleMoves:
            # this gives us the first 9 moves (and opening boards)
            turn  = 'X' #must switch between the players X and O 
            self.InitializedBoard() #initialize a board.  

            if self.boardDict[firstmove] == ' ':
                self.boardDict[firstmove] = turn
                self.count += 1
                turn = 'O'
                # could continue this to get the first move, but need to this for all the choices.. 

        # save the results. 




#Notes: 
self.boardDict gives : {'A1': ' ', 'A2': ' ', 'A3': ' ', 'B1': ' ', 'B2': ' ', 'B3': ' ', 'C1': ' ', 'C2': ' ', 'C3': ' '}





  


    # run a complete simulation 
        #but try to use some shortcut to shorten the time for running a complete simulation 
        #some board positions will be repetitive  





