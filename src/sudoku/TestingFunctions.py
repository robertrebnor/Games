from functions import *


# `grid` is defined in the test code scope as the following:
# (note: changing the value here will _not_ change the test code)
# grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'


display(grid)

# plot the game board 
display(grid_values_StartingBoard(grid))

# plot the game borad, with "123456789" instead of "."
display(grid_values(grid))

# plot the game borad, with only the possible numbers instead of "."
display(eliminate(grid_values(grid)))

# only choice
display( only_choice( eliminate(grid_values(grid))  ) )
print("end")

display( only_choice (only_choice( eliminate(grid_values(grid))  )) )

display( only_choice (only_choice (only_choice( eliminate(grid_values(grid))  )) ))

#solving the puzzle
display(reduce_puzzle(grid_values(grid)))

## Testing a harder sudoku
grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
values = grid_values(grid2)

# plot the game board 
display(grid_values_StartingBoard(grid2))


#Solution using search - depth-first search (DFS)
display( search(values) )


display( random_puzzle(N=17))

"""
import random


rows = 'ABCDEFGHI' #labels the rows on the board
cols = '123456789' #labels the cols on the board
digits =  cols

def cross(a, b):
    #   
    #Returns any combinaton of elements from two variables
    #
    return [s+t for s in a for t in b]

# A box is one single cell on the board, boxes creat all the single cells on the board
boxes = cross(rows, cols)
squares = boxes

values = dict((s, digits) for s in squares)

seq = list(values)
random.shuffle(seq)

"""