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
BoardBoxesList = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'A1', 'B2', 'C3', 'A3', 'B2', 'C3']

from moves import MovesOnBoard

class AgentPrograms(MovesOnBoard):

    def __init__(self):
        super().__init__()
        self.startingBoard = self.BoxesAndValues(self.boxes, self.emptyBoardValues) #the board a player customize to analyze a specific situation on the board
        self.CopyBoard = dict()
    
    def SearchNextMove(self):
        """Used by agents to search one move ahead.
        """
        # first test if it is possible to win in one move
        turn = self.turn
        MoveFound = None
        count = self.count

        if count >= 5:
            WinningMove = self.WinInOne()

            if WinningMove != None: #then we can win in one move
                self.boardDict[WinningMove] = turn
                self.DisplayBoard()
                print('\nGame Over.\n')
                print('Player ' + turn + ' has won the game')
                print('The winning combination is ' +   ', '.join(self.SolutionDict[self.WinningCombo])  )
                MoveFound = "winning_move"
                return MoveFound
            
        # secondly, check if it is possible to lose in the next move.
        if count >= 4:
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

        return MoveFound

    #def OnePlayerAgent(self):
    #    """Analyzes one move ahead
    #    """
    #    self.turn = self.SymbolComputer1
    #    print(" ")
    #    print("The computer does a move:")
    #    FoundMove = self.SearchNextMove()



    def NextMoveAgent(self):
        #self.NumberOfPlayers()
        #self.PlayerSymbols() 

        if self.NumbPlayers == 0:
   
            self.turn = 'X'
            self.DisplayBoard()
        
            for i in range(10):
                print('')

                self.count += 1
                print('--------------------------')
                print('Let us do move: ', self.count)
                FoundMove = self.SearchNextMove()
                
                if FoundMove == "winning_move":
                    break
    
    #def AgentTraning(self):
    #    """A function to train the agent progrem to figure out the optimal moves.
    #
    #    """

    def AnalyzeSpecificBoard(self):
        """Given a specific board, the function will find the optimal next move.
        """
        self.MakeCopyBoard(self.startingBoard)
        CopyBoard = self.CopyBoard
        print("")
        print("Welcome to analyze a custom board!")
        print("Let us start by setting up the board to be analyzed")
        self.DisplayBoard(CopyBoard) #Show an empty starting board

        player1 = "X"
        player2 = "0"
        turn = player1

        print("In this game Player 1 is 'X' and Player 2 is 'O'.")
        print("The first move is by Player 1, the second by Player 2 and so on until you have reached the wanted possition on the board.")
        print("When finished setting up the board, please type in 'analyze'. ")

        #This should be an own function in the PlayerInput_Module
        print('')
        SetUpStatus = "customizing"
        
        while SetUpStatus == "customizing":
            while True:
                move = input("Please chose a move for " + turn + " :").capitalize()

                if move not in BoardBoxesList and move != "Analyze":
                    print('Sorry, you have not typed an appropriate choice.')
                else:
                    #the choice is successfully parsed and accepted.
                    break
            
            if move == "Analyze":
                SetUpStatus = "Analyze"
                break
        
            if self.CopyBoard[move] == ' ':
                self.CopyBoard[move] = turn
                self.count += 1
                self.DisplayBoard(CopyBoard)

                # If the game is not over, we must change player to move
                if self.count == 10:
                    print("The board is full. Nothing to analyze.")
                    break
                elif turn =='X':
                    turn = 'O'
                else:
                    turn = 'X'

            else:
                print("That place is already filled.\nPlease select another move.")
                continue
               

        

            
        print('End of code')
    
        

    