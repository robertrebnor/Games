

import copy
import random

from inputs import PlayerInput


class MovesOnBoard(PlayerInput):

    def __init__(self):
        super().__init__()
    
    def MakeCopyBoard(self, OriginalBoard):
        """ Makes a deepcopy of a given board. 
        """
        self.CopyBoard = copy.deepcopy(OriginalBoard)

    def AvailableMove(self, board, box):
        """ Checks if a given box on a given board is an available move.

        Returns
        -------
            True if move is available. False if not. 
        """
        return board[box] == ' '

    def CheckSolutionInOneMove(self, SymbolMove):
        """ Uses a copy of the 'boardDict' to analyze if possible next moves results in 
        a winning move.

        Args
        ----
        SymbolMove: string
            Is 'X' or 'O'.

        Returns:
        -------
            A box resulting in a winning move if it exists, returns 'None' if 
            no winning move is found.        
        """
        for box in self.CopyBoard.keys():
            self.MakeCopyBoard(self.boardDict)
            CopiedBoard = self.CopyBoard
            
            if self.AvailableMove(CopiedBoard, box) == True:   
                if self.AgentPossibleWinningMove(CopiedBoard, box, SymbolMove) == True:
                    return box
        return None

    
    def WinInOne(self):
        """ Checks if there is a possible win in one move.

        Returns:
        -------
            A box resulting in a winning move if it exists, returns 'None' if 
            no winning move is found.    
        """
        turn = self.turn

        return self.CheckSolutionInOneMove(turn)

    # Combine this with WinInOne
    def LoseInOne(self):
        """ Check if there is a possible move resulting in losing the game. 
        
        Returns:
        -------
            A box resulting in a winning move if it exists, returns 'None' if 
            no winning move is found.    
        """
        turn = self.turn
    
        if turn == 'X':
            oppositeTurn = 'O'
        else:
            oppositeTurn = 'X'
        
        return self.CheckSolutionInOneMove(oppositeTurn)

    
    def TakeCorner(self):
        """ Checks if one of the corners is a possible move.

        Returns:
        -------
            Returns a corner box, if a corner box is a possbile move.
            Returns 'None' if no corner is available. 
        """

        self.MakeCopyBoard(self.boardDict)
        CopyBoard = self.CopyBoard

        AllCornerBoxes = ['A1', 'C1', 'A3', 'C3']
        PossibleMoves = []

        for box in AllCornerBoxes:
            if self.AvailableMove(CopyBoard, box) == True:
                PossibleMoves.append(box)
        
        if not PossibleMoves: #if no possible corner moves
            return None 
        if PossibleMoves:
            return random.choice(PossibleMoves)


    def TakeCenter(self): 
        """ Checks if the center is a possible move.

        Returns:
        -------
            Returns the center box, the center box is a possbile move.
            Returns 'None' if the center box is not available. 
        """
        self.MakeCopyBoard(self.boardDict)
        CopyBoard = self.CopyBoard
        CenterBox = 'B2'

        if self.AvailableMove(CopyBoard, CenterBox) == True:
            return CenterBox
        else:
            return None


    def TakeSide(self):
        """ Checks if one of the side boxes is a possible move.

        Returns:
        -------
            Returns a side box, if a side box is a possbile move.
            Returns 'None' if no side boxes is available. 
        """
        self.MakeCopyBoard(self.boardDict)
        CopyBoard = self.CopyBoard

        AllSideBoxes = ['B1', 'A2', 'C2', 'B3']
        PossibleMoves = []

        for box in AllSideBoxes:
            if self.AvailableMove(CopyBoard, box) == True:
                PossibleMoves.append(box)
        
        if not PossibleMoves: #if no possible corner moves
            return None 
        if PossibleMoves:
            return random.choice(PossibleMoves)


    #def AnalyzeSpecificMoves(self):
    #    """Not completed 
    #    """
    #    AllCornerBoxes = ['A1', 'C1', 'A3', 'C3']
    #    CenterBox = 'B2'
    #    AllSideBoxes = ['B1', 'A2', 'C2', 'B3']
    #
    #    self.MakeCopyBoard(startingBoard)
    #    CopyBoard = self.CopyBoard

    
    