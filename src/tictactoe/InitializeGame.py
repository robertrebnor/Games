#################################  
# File: Initialize Game         #
# Program in: Tic tac toe game  #
# Main program: MainProgram     #
#                               #
# By: Robert Rebnor             #
#                               #
#################################
"""
Goal

"""

def cross(rows, cols):
    """
    Returns any combination of elements from two variables 
    """
    return [s+t for s in cols for t in rows]

class setGame():

    def __init__(self):
        """

        """
        # Define the rows and the cols of the board
        self.rows = rows = '123'
        self.cols = cols = 'ABC'
        self.grid = '         '

        # Define a "name" for each box on the board
        self.boxes = cross(rows, cols)

        # Create a list with a list of all the boxes in a row
        self.row_units = [ cross(r, cols) for r in rows ]

        # Create a similar list for columns
        self.column_units = [ cross(rows, c) for c in cols]

        

