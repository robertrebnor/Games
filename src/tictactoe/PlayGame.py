#################################  
# File: Play Game               #
# Program in: Tic tac toe game  #
# Main program: MainProgram     #
#                               #
# By: Robert Rebnor             #
#                               #
#################################

import DisplayGame as DisplayGame
import SolveGame as SolveGame

SolutionDict = {'Across the top': ['A1', 'B1', 'C1'],
                'Across the middle': ['A2', 'B2', 'C2'],
                'Across the bottom': ['A3', 'B3', 'C3'],
                'Down the left side': ['A1', 'A2', 'A3'],
                'Down the middle': ['B1', 'B2', 'B3'],
                'Down the right side': ['C1', 'C2', 'C3'],
                'Left down diagonal': ['A1', 'B2', 'C3'],
                'Left up diagonal': ['A3', 'B2', 'C3']
            }


class PlayGame(DisplayGame.DisplayGame):

    def __init__(self):
        super().__init__()

    def Play(self):
        print('')
        print('Let us play Tic Tac Toe.')

        DisplayGame.DisplayGame.DisplayBoard(self)

        turn = 'X'
        self.count = 0

        print("Now let's start playing.")

        self.boardDict = boardDict = DisplayGame.grid_values_StartingBoard(self.grid, self.boxes)
        
        for i in range(10):
            print('')
            print("It's your turn, " + turn + ". Move to which place?")

            move = input().capitalize()

            if boardDict[move] == ' ':
                boardDict[move] = turn
                self.count += 1
                DisplayGame.display(self.boxes, self.rows, self.cols, boardDict)
            else:
                print("That place is already filled.\nMove to which place?") #write a better text here
                continue
            
            # After every successful move, we must check if someone has won - PUT THIS IN OWN CLASS
             #count = self.count 
            
            gameWon = None
            # Now we will check if player X or O has won,for every move after 5 moves. 
            if self.count >= 5:
                for x in SolutionDict.keys():
                    SolutionList = SolutionDict[x]
                    if boardDict[ SolutionList[0] ] == boardDict[ SolutionList[1] ] == boardDict[ SolutionList[2]] != ' ':
                        print('\nGame Over.\n')
                        print('Player ' + turn + ' has won the game')
                        print('The winning combination is: ' + x + '. With the boxes: ' + SolutionList[0] + ', ' + SolutionList[1] + ', ' + SolutionList[2] )
                        gameWon = "done"
                        break 
                if gameWon == "done":
                    break
                # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
                if self.count == 9:
                    print("\nGame Over.\n")                
                    print("It's a Tie!!")


            # If the game is not over, we must change player to move
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X' 