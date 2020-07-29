

import copy
import random

import PlayerInput as PlayerInput

class MovesOnBoard(PlayerInput.PlayerInput):

    def __init__(self):
        super().__init__()
    
    def MakeCopyBoard(self, OriginalBoard):
        self.CopyBoard = copy.deepcopy(OriginalBoard)

    def AvailableMove(self, board, box):
        return board[box] == ' '

    def WinInOne(self):
        turn = self.turn
        
                   
        for box in self.CopyBoard.keys():
            self.MakeCopyBoard(self.boardDict)
            CopiedBoard = self.CopyBoard
            
            if self.AvailableMove(CopiedBoard, box) == True:   
                if self.AgentPossibleWinningMove(CopiedBoard, box, turn) == True:
                    return box
    
        return None
    
    
    def LoseInOne(self):
        turn = self.turn
    
        if turn == 'X':
            oppositeTurn = 'O'
        else:
            oppositeTurn = 'X'

        for box in self.CopyBoard.keys():
            self.MakeCopyBoard(self.boardDict)
            CopiedBoard = self.CopyBoard
    
            if self.AvailableMove(CopiedBoard, box) == True:
                if self.AgentPossibleWinningMove(CopiedBoard, box, oppositeTurn) == True:
                    return box
        return None
    
    def TakeCorner(self):
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
        self.MakeCopyBoard(self.boardDict)
        CopyBoard = self.CopyBoard
        CenterBox = 'B2'

        if self.AvailableMove(CopyBoard, CenterBox) == True:
            return CenterBox
        else:
            return None


    def TakeSide(self):
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

    
    