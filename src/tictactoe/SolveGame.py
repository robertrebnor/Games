#################################  
# File: Solve Game              #
# Program in: Tic tac toe game  #
# Main program: MainProgram     #
#                               #
# By: Robert Rebnor             #
#                               #
#################################

import DisplayGame as DisplayGame


class SolveGame(DisplayGame.DisplayGame):

    def __init__(self):
        super().__init__()

        self.SolutionDict = {'Across the top': ['A1', 'B1', 'C1'],
                            'Across the middle': ['A2', 'B2', 'C2'],
                            'Across the bottom': ['A3', 'B3', 'C3'],
                            'Down the left side': ['A1', 'A2', 'A3'],
                            'Down the middle': ['B1', 'B2', 'B3'],
                            'Down the right side': ['C1', 'C2', 'C3'],
                            'Left down diagonal': ['A1', 'B2', 'C3'],
                            'Left up diagonal': ['A3', 'B2', 'C3']
                        }
        self.WinningCombo = None

    def Solver(self, UseCopyBoard = False):

        count = self.count 
        if UseCopyBoard == True:
            boardDict = self.CopyBoard
        elif UseCopyBoard == False:
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
                print("\nGame Over.\n")                
                print("It's a tie.")

    