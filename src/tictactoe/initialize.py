#################################  
# Module: initialize            #
# Program in: Tic tac toe game  #
# Main program: MainProgram     #
#                               #
# By: Robert Rebnor             #
#                               #
#################################
"""
Goal

"""

class setGame():

    def __init__(self):
        """Initialize the basic attributes need to work with the board
        """
        # Define the rows and the cols of the board
        self.rows = rows = '123'
        self.cols = cols = 'ABC'
        self.emptyBoardValues = '         ' #do not need a grid, just use the BoardDict from the start?

        # Define a "name" for each box on the board
        self.boxes = self.CreateBoxes(rows, cols)

        # Create a list with a list of all the boxes in a row
        self.row_units = [ self.CreateBoxes(r, cols) for r in rows ]

        # Create a similar list for columns
        self.column_units = [ self.CreateBoxes(rows, c) for c in cols]

        # Other 
        #self.turn = None
        #self.count = 0   
        #self.boardDict = self.BoxesAndValues(boxes, emptyBoardValues)
        #self.CopyBoard = dict()
        #self.gameWon = None
        
    def CreateBoxes(self, rows, cols):
        """Combining the rows and cols to create an index for each cell (box) on the board. 
        """
        # Returns any combination of elements from two variables 
        return [s+t for s in cols for t in rows]
    
    def BoxesAndValues(self, boxes, grid): # grid_values_StartingBoard(grid, boxes)
        """Convert grid string into {<box>: <value>} dict with '.' value for empties.

        Args:
            grid:  grid in string form, 9 characters long
        Returns:
            
            - keys: Box labels, e.g. 'A1'
            - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
        """
        #check that grid contains the correct length 
        assert len(grid) == 9

        #Connect one value in for the grid to a specific box by using a dictionary 
        return dict(zip(boxes, grid))





