#################################  
# File: Display Game            #
# Program in: Tic tac toe game  #
# Main program: MainProgram     #
#                               #
# By: Robert Rebnor             #
#                               #
#################################

import InitializeGame as InitializeGame


def grid_values_StartingBoard(grid, boxes):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    #check that grid contains the correct length 
    assert len(grid) == 9

    #Connect one value in for the grid to a specific box by using a dictionary 
    return dict(zip(boxes, grid))


def display(boxes, rows, cols, values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    
    width = 1+max(len(values[s]) for s in boxes)
    line = '  ' + '+'.join(['-'*(width)]*3)

    for r in rows:
        if r in 'A':
            print('  A  B  C ')
        print( (r + ' ' ) +  ''.join(values[r+c].center(width)+('|' if c in '12' else '')
                    for c in cols))
        if r in 'AB': print(line)
    return



class DisplayGame(InitializeGame.setGame):

    def __init__(self):
        super().__init__()
    
    def DisplayBoard(self): #change to DisplayStaringboard
        values = grid_values_StartingBoard(self.grid, self.boxes)
        display(self.boxes, self.rows, self.cols, values)
    
    #def DisplayPlayingBoard(self, moves):




        