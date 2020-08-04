#################################  
# Module: initialize            #
# Program in: Tic tac toe game  #
# Main module: tictactoe_main   #
#                               #
# By: Robert Rebnor             #
#                               #
#################################
"""In this module:

Goal
----
    * Set up the attributes and the functions need to set up the game board. 

Functions
---------
    __init__: Set up basic attributes need to set up the game board.
    CreateBoxes: Combines rows and cols to create the each box on the board.
    BoxesAndValues: Creates a dict containing the boxes and the value in each box.
"""

class setGame():

    def __init__(self):
        """Initialize the basic attributes need to create a board. 

        Attributes
        ----------
        rows : string
            Enumerates the rows from 1 to 3. 
        cols : string
            Names the columns with A,B and C.
        emptyBoardValues : string
            An empty string of length 9 used to create an empty game board.
        boxes : list
            Contains all the boxes on the board. 
        row_units : list 
            A list with a list for each row.
        column_units : list 
            A list with a list for each column.
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

    def CreateBoxes(self, rows, cols):
        """Combining the rows and cols to create an index for each cell (box) on the board. 

        Args
        ------
        rows : string
            A string with the row numbers
        cols : string
            A string with the name of the columns.

        Returns
        -------
            A list with the all boxes combined from the rows and cols given.

        """
        return [s+t for s in cols for t in rows]
    
    def BoxesAndValues(self, boxes, grid):
        """ Creates a dict {<box>: <value>}. 
        

        Convert grid string into {<box>: <value>} dict with '.' value for empties.

        Args
        -----
        boxes: list
            A list with the name of the boxes on the board. 
        grid: string
            The values to be combined with boxes on the board. 
            For the initial board, the string is an empty and 9 characters long.

        Returns
        --------
        A dict: 
            The keys are the name of the boxes on the board.
            The values are the input on a given box.
        """
        assert len(grid) == 9

        return dict(zip(boxes, grid))
