

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





for i in range(10):
    print(i)
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

testeDict = {'Across the top': ['A1', 'B1', 'C1'],
            'Across the middle': ['A2', 'B2', 'C2'],
            'Across the bottom': ['A3', 'B3', 'C3']
            }

testeDict.keys()

for x in testeDict.keys():
    print(testeDict[x])
print('test done')


for x in testeDict.keys():
    listTest = (testeDict[x])
    print(listTest[0])
    print(listTest[1])
    print(listTest[2])
print('test done')


SolutionDict = {'Across the top': ['A1', 'B1', 'C1'],
                'Across the middle': ['A2', 'B2', 'C2'],
                'Across the bottom': ['A3', 'B3', 'C3'],
                'Down the left side': ['A1', 'A2', 'A3'],
                'Down the middle': ['B1', 'B2', 'B3'],
                'Down the right side': ['C1', 'C2', 'C3'],
                'Left down diagonal': ['A1', 'B2', 'C3'],
                'Left up diagonal': ['A3', 'B2', 'C3']
            }

 


# Now we will check if player X or O has won,for every move after 5 moves. 
if self.count >= 5:
    for x in SolutionDict.keys():
        SolutionList = SolutionDict[x]
        if boardDict[ SolutionList[0] ] == boardDict[ SolutionList[1] ] == boardDict[ SolutionList[2]] != ' ':
            print('\nGame Over.\n')
            print('Player ' + turn + ' has won the game')
            print('The winning combination is: ' + x + '. With the boxes: ' + SolutionList[0] + ', ' + SolutionList[1] + ', ' + SolutionList[2] )
            break 

