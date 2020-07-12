#################################  
# File: Display Game            #
# Program in: Tic tac toe game  #
# Main program: MainProgram     #
#                               #
# By: Robert Rebnor             #
#                               #
#################################

import InitializeGame as InitializeGame

class DisplayGame(InitializeGame.setGame):

    def __init__(self):
        super().__init__()

    def DisplayBoard(self):
        boxes = self.boxes
        rows = self.rows
        cols = self.cols
        values = self.boardDict

        width = 1+max(len(values[s]) for s in boxes)
        line = '  ' + '+'.join(['-'*(width)]*3)

        for r in rows:
            if r in '1':
                print('  A  B  C ')
            print( (r + ' ' ) +  ''.join(values[c+r].center(width)+('|' if c in 'AB' else '')
                        for c in cols))
            if r in '12': print(line)
        return





        