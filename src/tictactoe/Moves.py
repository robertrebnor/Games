

import copy
import random

import PlayerInput as PlayerInput

class MovesOnBoard(PlayerInput.PlayerInput):

    def __init__(self):
        super().__init__()
    
    def MakeCopyBoard(self, OriginalBoard):
        #for box in OriginalBoard.keys():
        #    self.CopyBoard[box] = OriginalBoard[box]
        self.CopyBoard = copy.deepcopy(OriginalBoard)

    def AvailableMove(self, board, box):
        return board[box] == ' '

    def WinInOne(self):
        # Do not need this if count is less than 5
        count = self.count 
        turn = self.turn
        
        if count >= 5: 
            self.MakeCopyBoard(self.boardDict)
            CopyBoard = self.CopyBoard
            
            for box in CopyBoard.keys():
                if self.AvailableMove(CopyBoard, box) == True:
                    self.CopyBoard[box] = turn
                    self.Solver(UseCopyBoard = True)
                    if self.gameWon == "done":
                        return box
                    else:
                        return None
        else:
            return None
        

    def LoseInOne(self):
        # Do not need to apply this is count i less than 5
                # Do not need this if count is less than 5
        count = self.count 
        turn = self.turn
        if count >= 5: 
            if turn == 'X':
                oppositeTurn = 'O'
            elif turn == 'O':
                oppositeTurn = 'X'

            self.MakeCopyBoard(self.boardDict)
            CopyBoard = self.CopyBoard
            
            for box in CopyBoard.keys():
                if self.AvailableMove(CopyBoard, box) == True:
                    self.CopyBoard[box] = oppositeTurn
                    self.Solver(UseCopyBoard = True)
                    if self.gameWon == "done":
                        self.gameWon = None
                        return box
                    else:
                        return None
        else:
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


    
    