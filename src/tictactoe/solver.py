#################################  
# Module: solver                #
# Program in: Tic tac toe game  #
# Main module: tictactoe_main   #
#                               #
# By: Robert Rebnor             #
#                               #
#################################
"""In this module:

Goal
----
    * Check if a player as won the game.
    * Check an agent has a possible winning/losing move.

Functions
---------
    __init__: Set up last basic attributes need to display the game board with values in the boxes
    Solver: Checks if there is a winning combination on the board. 
    AgentPossibleWinningMove: Checks if there is a move to win the game.
"""

from display import DisplayGame


class SolveGame(DisplayGame):

    def __init__(self):
        """The initializer for solving the game module. 

        Attributes
        ----------
        SolutionDict: dict
            Keys: Name of the possible winning combinations.
            Values: The boxes in a winning combination.
        WinningCombo: str
            Default: None
            Changes to the name of a winning combination when a winning combination is found.
        turn: str
            Default: None
            Changes to 'X' or 'O' depending on players.
        gameWon: str
            Default: None
            Changes to 'done' when a winning combinaton is found.
        count: int
            Default: zero
            Counts the number of moves made on the board.
        """
        super().__init__()

        self.SolutionDict = {'Across the top': ['A1', 'B1', 'C1'],
                            'Across the middle': ['A2', 'B2', 'C2'],
                            'Across the bottom': ['A3', 'B3', 'C3'],
                            'Down the left side': ['A1', 'A2', 'A3'],
                            'Down the middle': ['B1', 'B2', 'B3'],
                            'Down the right side': ['C1', 'C2', 'C3'],
                            'Left down diagonal': ['A1', 'B2', 'C3'],
                            'Left up diagonal': ['A3', 'B2', 'C1']
                        }
        self.WinningCombo = None
        self.turn = None
        self.gameWon = None
        self.count = 0   

    def Solver(self):
        """ Checks if there is a winning combination on the game board.
        Needs at least five moves on the game board to check for a winning combination.
        If the game board is full (nine moves done) and no winning combination is found,
        the game is a tie.
        """

        count = self.count 
        boardDict = self.boardDict
        
        SolutionDict = self.SolutionDict
        if count >= 5:
            for x in SolutionDict.keys():
                SolutionList = SolutionDict[x]
                if boardDict[ SolutionList[0] ] == boardDict[ SolutionList[1] ] == boardDict[ SolutionList[2]] != ' ':
                    self.gameWon = "done"
                    self.WinningCombo = x
                    break 
           
            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                DisplayGame.DisplayTieMessage()

    def AgentPossibleWinningMove(self, CopiedBoard, box, turn):
        """ Given the positions on a game board, checks if there is possible winning move. 

        Args
        -----
        CopiedBoard: dict
            A dict with the boxes and values from the game board to analyze. 
        box: str
            The box on board we want check if it is a winning move.
        turn: str
            Either 'X' or 'O', depending on which winning move we are testing. 

        Return
        ------
        Returns True if the given box and move is a winning combination. Returns False
        if not. 
        """
        boardDict = CopiedBoard
        SolutionDict = self.SolutionDict
        boardDict[box] = turn     
  
        for x in SolutionDict.keys():
            SolutionList = SolutionDict[x]
            if boardDict[ SolutionList[0] ] == boardDict[ SolutionList[1] ] == boardDict[ SolutionList[2]] != ' ':
                #self.gameWon = "done"
                self.WinningCombo = x
                return True 
        return False    