    


from humans import PlayWithPlayers
from agents import AgentPrograms




class PlayGame(PlayWithPlayers, AgentPrograms):

    def __init__(self):
        super().__init__()
    
    #this must be put in another module
    def OnePlayerOneAgent(self):
        print('')
        print('Let us play Tic Tac Toe.')
        #self.NumberOfPlayers()
        #self.PlayerSymbols()
        self.turn = self.WhoGoesFirst()
        self.count = 0  #count the number of moves made in the game    
        self.DisplayBoard()

        print("Symbol player:", self.SymbolPlayerOne)
        print("Symbol computer:", self.SymbolComputer1)
        print("Player ", self.turn , " starts the game.")

        for i in range(10):
            print('')
            WinningMovedFound = None
            if self.turn == self.SymbolComputer1:
                # Call computer move:
                self.count += 1
                WinningMovedFound = self.SearchNextMove()
                
            elif self.turn == self.SymbolPlayerOne:      
                # Call player input:
                self.GetPlayersMove()
                if self.gameWon != "done":
                    if self.turn =='X':
                        self.turn = 'O'
                    else:
                        self.turn = 'X'
                
            
            if WinningMovedFound == "winning_move": #the computer has found a winning move
                break
        
            # After every successful move, we must check if someone has won - PUT THIS IN OWN CLASS
            self.Solver()

            if self.gameWon == "done":
                print('\nGame Over.\n')
                print('Player ' + self.turn + ' has won the game')
                print('The winning combination is ' +   ', '.join(self.SolutionDict[self.WinningCombo])  )
                break 
           
            
    # humans most be able to play two humans against each other and one human against an agent
    # agents must be able to play against another agent, against a human and simulate game. 

    # this file fixes easy functions for all possible options to play.

    def TestingGameOptions(self):
        self.NumberOfPlayers()
        self.PlayerSymbols() 

        playersInGame = self.NumbPlayers

        if playersInGame == 0:
            self.NextMoveAgent()
        
        elif playersInGame == 1:
            self.OnePlayerOneAgent()

        elif playersInGame == 2:
            self.TwoPlayerGame()
        else:
            print("Something is wrong.")

# need to think about cleaning board after finished playing, so it is possible to play multiple times.


startgame = PlayGame()