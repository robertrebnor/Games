

import InitializeGame as InitializeGame

testObj = InitializeGame.setGame()


rows = testObj.rows
cols = testObj.cols

cell = testObj.boxes

#starting with an empty board:
#symbols for playing x and o

values = '#########'
values2 = '         '

values = dict(zip(cell, values))
values2 = dict(zip(cell, values))

width = 1+max(len(values[s]) for s in cell)
line = '  ' + '+'.join(['-'*(width)]*3)

len(line)


for r in rows:
    if r in 'A':
        print('  A  B  C ')
        print('')
    print( (r + ' ' ) +  ''.join(values[r+c].center(width)+('|' if c in '12' else '')
                for c in cols))
    if r in 'AB': print(line)
print('done')



 # | # | # 
---+---+---
 # | # | # 
---+---+---
 # | # | # 


for i in range(10):
    print(i)
print('done')



# The different winning combinations:

# Across the top:


# Now we will check if player X or O has won,for every move after 5 moves. 
if self.count >= 5:
    if boardDict['A1'] == boardDict['A2'] == boardDict['A3'] != ' ': # across the top
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")                
        break
    elif boardDict['B1'] == boardDict['B2'] == boardDict['B3'] != ' ': # across the middle
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break
    elif boardDict['C1'] == boardDict['C2'] == boardDict['C3'] != ' ': # across the bottom
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break
    elif boardDict['A1'] == boardDict['B1'] == boardDict['C1'] != ' ': # down the left side
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break
    elif boardDict['A2'] == boardDict['B2'] == boardDict['C2'] != ' ': # down the middle
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break
    elif boardDict['A3'] == boardDict['B3'] == boardDict['C3'] != ' ': # down the right side
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break 
    elif boardDict['A1'] == boardDict['B2'] == boardDict['C3'] != ' ': # diagonal
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break
    elif boardDict['C1'] == boardDict['B2'] == boardDict['A3'] != ' ': # diagonal
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break 