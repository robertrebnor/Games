#################################  
# Module: display               #
# Program in: Tic tac toe game  #
# Main module: tictactoe_main   #
#                               #
# By: Robert Rebnor             #
#                               #
#################################
"""In this module:

Goal
----
    * Display the board with values in the boxes. 

Functions
---------
    __init__: Set up last basic attributes need to display the game board with values in the boxes
    DisplayBoard: Displays the game board with values in the boxes. 
"""

from initialize import setGame

class DisplayGame(setGame):

    def __init__(self):
        """ Initializes empty board dict to display the game board.
        """
        super().__init__()
        self.boardDict = self.BoxesAndValues(self.boxes, self.emptyBoardValues)

    def DisplayBoard(self, CustomBoard = None):
        """ Displays the game board with possible values in the boxes.

        Args
        ----
        CustomBoard: dict
            Default: None
            Gives the possibility to display another board than the attributed board 'boardDict'.
        """
        boxes = self.boxes
        rows = self.rows
        cols = self.cols
        if CustomBoard != None:
            values = CustomBoard
        else: 
            values = self.boardDict

        width = 1+max(len(values[s]) for s in boxes)
        line = '  ' + '+'.join(['-'*(width)]*3)

        for r in rows:
            if r in '1':
                print('  A  B  C ')
            print( (r + ' ' ) +  ''.join(values[c+r].center(width)+('|' if c in 'AB' else '')
                        for c in cols))
            if r in '12': print(line)
        #return





        