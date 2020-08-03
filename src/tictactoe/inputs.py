#################################  
# File: Play Game               #
# Program in: Tic tac toe game  #
# Main program: MainProgram     #
#                               #
# By: Robert Rebnor             #
#                               #
#################################

from random import randint


from solver import SolveGame

class PlayerInput(SolveGame):

    def __init__(self):
        super().__init__()

    def NumberOfPlayers(self):
        print('Please select the number of players for the game.')
        print('Choose between:')
        print('   0. Both players are computers.')
        print('   1. One player and one computer.')
        print('   2. Two players.')
        while True:
            try:
                print('Select between 0, 1 and 2 players.')
                self.NumbPlayers = int(input('Please enter your choice: '))
            except ValueError:
                print('Your choice must be a number.')
                continue
            if self.NumbPlayers < 0 or self.NumbPlayers > 2:
                print('Choice not recognize.')
                print('You have to choose between 0, 1 or 2.')
                continue
            else:
                #the choice is successfully parsed and accepted.
                break
    def ReadInSymbolPlayer(self):
        while True:
            print('Choose between the symbols X or O.')
            self.SymbolPlayerOne = input('Please enter the symbol for player 1: ').upper()

            if self.SymbolPlayerOne not in ('X', 'O'):
                print('Sorry, you have not typed an appropriate symbol.')
            else:
                #the choice is successfully parsed and accepted.
                break

    def PlayerSymbols(self):
        SelectedNumberPlayers = self.NumbPlayers

        if SelectedNumberPlayers == 0:
            self.computerOne = 'X'
            self.computerTwo = 'O'
        
        elif SelectedNumberPlayers == 1:
            self.ReadInSymbolPlayer()
            if self.SymbolPlayerOne == 'X':
                self.SymbolComputer1 = 'O'
            elif self.SymbolPlayerOne == 'O':
                self.SymbolComputer1 ='X'

        elif SelectedNumberPlayers == 2:
            self.ReadInSymbolPlayer()
            if self.SymbolPlayerOne == 'X':
                self.SymbolPlayerTwo = 'O'
            elif self.SymbolPlayerOne == 'O':
                self.SymbolPlayerTwo ='X'

    def WhoGoesFirst(self):
        """Choses which player that starts at random
        """
        if randint(0,1) == 1:
            return 'X'
        else: 
            return 'O'



   
        
