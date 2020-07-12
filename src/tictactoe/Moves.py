

import SolveGame as SolveGame

class PossibleMoves(SolveGame.SolveGame):

    def __init__(self):
        super().__init__()

    def MoveAvailable(self):
        return self.CopyBoard == ' '


class NextMoves():

    def __init__(self):
        super().__init__()

    def WinInOne(self):
        # Do not need this if count is less than 5
        count = self.count 
        CopyBoard = self.CopyBoard

        if count >= 5: 
            if MoveAvailable(self) == True:
                SolveGame.SolveGame.Solver(self)
        else:
            return False 
        



 # Check if the player could win on their next move, and block them.

113.     for i in range(1, 10):

114.         copy = getBoardCopy(board)

115.         if isSpaceFree(copy, i):

116.             makeMove(copy, playerLetter, i)

117.             if isWinner(copy, playerLetter):

118.                 return i

119.

    def LoseInOne():
        # Do not need to apply this is count i less than 5

    def TakeCorner():
        #Corners: A1 C1 A3 C3

    def TakeCenter():
        #Center: B2

    def TakeSide():
        # Sides: B1 A2 C2 B3

    
    