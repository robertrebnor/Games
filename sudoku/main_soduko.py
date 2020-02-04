from functions import display, grid_values_StartingBoard, grid_values, eliminate, search

menu = { }
menu['1'] = "Start a random game." 
menu['2'] = "Start a custom game."
menu['3'] = "Get a solution to a custom game"
menu['4'] = "Exit program"

levelGame = { }
levelGame['1'] = 'Easy'
levelGame['2'] = 'Medium'
levelGame['3'] = 'Hard'
levelGame['4'] = 'Go back to main meny'
levelGame['5'] = 'Exit program'

solutionGame = { }
solutionGame['1'] = "Show hints."
solutionGame['2'] = "Show solution."
solutionGame['3'] = 'Go back to main meny'
solutionGame['4'] = 'Exit program'

while True:
    print(" Welcome to Sudoku!")
    print(" ")
    #options = menu.keys()
    #options.sort()
    for entry in menu:
        print(" ", entry,".", menu[entry])
    print("")
    selection=  input("Please type in the number of your choice: ") 
    if selection =='1': 
        print(" ")
        print("You can play Sudoku at the following levels:") 
        for i in levelGame:
            print(i,".",levelGame[i])
        while True:
            print("")
            selc_levGame =  input("Please type in the number of your choice:  ") 
            if selc_levGame == "1":
                printBoard = True
                while True:
                    if printBoard == True:
                        print(" ")
                        print(" Sudoku game: Easy ")
                        print(" ")
                        ## Add this to be a random drawn board 
                        grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
                        display(grid_values_StartingBoard(grid))
                    print(" ")
                    for i in solutionGame:
                        print(i,".", solutionGame[i])
                    solutionGame_choice =  input("Please type in the number of your choice:  ") 
                    if solutionGame_choice == "1":
                        display(eliminate(grid_values(grid)))
                        printBoard = False
                    elif solutionGame_choice == "2":
                        display( search( grid_values(grid) ) )
                        printBoard = False
                    elif solutionGame_choice == "3":
                        break
                    elif solutionGame_choice == "4":
                        exit()
            elif selc_levGame == "2":
                print("Option not defined yet")
                #fix this
            elif selc_levGame == "3":
                print("Option not defined yet")
            elif selc_levGame == "4":
                break
            elif selc_levGame == "5":
                exit()
            else: 
                print ("Unknown Option Selected!" )
    elif selection == '2': 
      print ("delete")
    elif selection == '3':
      print ("find") 
    elif selection == '4': 
      exit()
    else: 
      print ("Unknown Option Selected!" )


