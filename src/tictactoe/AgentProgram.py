#################################  
# File: Agent program           #
# Program in: Tic tac toe game  #
# Main program: MainProgram     #
#                               #
# By: Robert Rebnor             #
#                               #
#################################

# Add:
#Search Tree


import Moves as Moves

class AgentPrograms(Moves.MovesOnBoard):

    def __init__(self):
        super().__init__()

    def NextMoveAgent(self):
        self.NumberOfPlayers()
        self.PlayerSymbols() 

        if self.NumbPlayers == 0:

            self.count = 0  #count the number of moves made in the game    
            self.turn = turn = 'X'
            self.DisplayBoard()
        
            for i in range(10):
                print('')

                self.count = i + 1
                MoveFound = None

                # must test to find which move to do

                # first test if it is possible to win in one move
                WinningMove = self.WinInOne()
                if WinningMove != None: #then we can win in one move
                    self.boardDict[WinningMove] = turn
                    self.DisplayBoard()
                    print('\nGame Over.\n')
                    print('Player ' + turn + ' has won the game')
                    print('The winning combination is ' +   ', '.join(self.SolutionDict[self.WinningCombo])  )
                    break
                
                # secondly, check if it is possible to lose in the next move.
                StopLosingMove = self.LoseInOne()
                if StopLosingMove != None: 
                    self.boardDict[StopLosingMove] = turn
                    self.DisplayBoard()
                    MoveFound = 'yes'
                
                # thirdly, check the corners 
                if MoveFound == None:
                    PlaceCornerMove = self.TakeCorner()
                    if PlaceCornerMove != None:
                        self.boardDict[PlaceCornerMove] = turn
                        self.DisplayBoard()
                        MoveFound = 'yes'

                # fourthly, check if the center is available
                if MoveFound == None:
                    PlaceCenter = self.TakeCenter()
                    if PlaceCenter != None:
                        self.boardDict[PlaceCenter] = turn
                        self.DisplayBoard()
                        MoveFound = 'yes'

                if MoveFound == None:
                    # fifthly, check the sides
                    PlaceSide = self.TakeSide()
                    if PlaceSide != None:
                        self.boardDict[PlaceSide] = turn
                        self.DisplayBoard()

                if self.count == 9:
                    print("\nGame Over.\n")                
                    print("It's a tie.")

                # If the game is not over, we must change player to move
                if turn =='X':
                    self.turn = turn = 'O'
                else:
                    self.turn = turn = 'X'
        