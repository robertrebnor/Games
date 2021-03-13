

import initialize as InitializeGame

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



# The different winning combinations:

# Across the top:       'A1' 'B1' 'C1'
# across the middle     'A2' 'B2' 'C2'
# across the bottom     'A3' 'B3' 'C3'

# down the left side    'A1' 'A2' 'A3'
# down the middle       'B1' 'B2' 'B3'
# down the right side   'C1' 'C2' 'C3'

# diagonal      'A1' 'B2' 'C3'
# diagonal      'A3' 'B2' 'C3'

testDict = {'A1': 'test1', 'A2': 'test2'}

for x in testDict.keys():
    print(x)
print('done')

print(testDict['A1'])

testList = ['a', 'b']


for i in range(10):
    print(i)
print('end')

PossibleMoves = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']

for i in range(len(PossibleMoves)):
    print(i)

for moves in PossibleMoves:
    print(moves)