


from inputs import PlayerInput

BoardBoxesList = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3', 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'A1', 'B2', 'C3', 'A3', 'B2', 'C3']

class PlayWithPlayers(PlayerInput):


    def __init__(self):
        super().__init__()

    def GetPlayersMove(self):
        turn = self.turn
        while True:
            move = input("It's your turn " + turn + ". Please select your move: ").capitalize()
            
            if move not in BoardBoxesList:
                print('Sorry, you have not typed an appropriate choice.')
                continue
            
            elif self.boardDict[move] == ' ':
                self.boardDict[move] = turn
                self.count += 1
                self.DisplayBoard()
                break
            else:
                print("That place is already filled.\nPlease select another move.")
                continue

    def TwoPlayerGame(self):
        print('')
        print('Let us play Tic Tac Toe.')
        #self.NumberOfPlayers()
        #self.PlayerSymbols()
        self.turn = self.WhoGoesFirst()
        self.count = 0  #count the number of moves made in the game    
        self.DisplayBoard()

        # this should be i = 1 as default and range(10)
        for i in range(9):
            print('')
                 
            # Call player input:
            self.GetPlayersMove()
    
            # After every successful move, we must check if someone has won - PUT THIS IN OWN CLASS
            self.Solver()

            if self.gameWon == "done":
                print('\nGame Over.\n')
                print('Player ' + self.turn + ' has won the game')
                print('The winning combination is ' +   ', '.join(self.SolutionDict[self.WinningCombo])  )
                break 
           
            # If the game is not over, we must change player to move
            if self.turn =='X':
                self.turn = 'O'
            else:
                self.turn = 'X'
    
