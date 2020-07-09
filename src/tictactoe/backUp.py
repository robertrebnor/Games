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

            move = input()        

            if boardDict[move] == ' ':
                boardDict[move] = turn
                self.count += 1
                DisplayGame.display(self.boxes, self.rows, self.cols, boardDict)
            else:
                print("That place is already filled.\nMove to which place?")
                continue
            
            # After every successful move, we must check if someone has won - PUT THIS IN OWN CLASS
             #count = self.count 
            
            # Now we will check if player X or O has won,for every move after 5 moves. 
            if self.count >= 5:
                if boardDict['A1'] == boardDict['A2'] == boardDict['A3'] != ' ': # across the top
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")                
                    break
                elif boardDict['B1'] == boardDict['B2'] == boardDict['B3'] != ' ': # across the middle
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif boardDict['C1'] == boardDict['C2'] == boardDict['C3'] != ' ': # across the bottom
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif boardDict['A1'] == boardDict['B1'] == boardDict['C1'] != ' ': # down the left side
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif boardDict['A2'] == boardDict['B2'] == boardDict['C2'] != ' ': # down the middle
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif boardDict['A3'] == boardDict['B3'] == boardDict['C3'] != ' ': # down the right side
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break 
                elif boardDict['A1'] == boardDict['B2'] == boardDict['C3'] != ' ': # diagonal
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif boardDict['C1'] == boardDict['B2'] == boardDict['A3'] != ' ': # diagonal
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
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