





# To do text:

# Comment better 
    # An overview of the different programs in MainProgram
    # Comment on the different programs, classes and functions

# Moves.py:
    # Find possible moves
    # Do the possible next moves

# AgentProgram.py:
    # NextMove (Only analyses to find the "best" next move)
    # SearchTree:
        # Looks a all possible next moves and analyzes which of these moves that are the optimal move
        # Note 1: Must always first check if we can win in one move or lose in one move. If true, then this is the best move.
        # Note 2: Apply utility, 1 = win, 0 = tie, -1 = loss 

# GameMenu.py:
    # Add the choice between: 1 player, 2 player and 2 agents simulating a given number of games
    # Add the possibility of playing another game when finished
        # If a new game, store the number of games played and stats for those games
    # Add the choice of which agent program to be used in the game


import tictactoe_main as ttt

TestAgentProgram = ttt.startgame

TestAgentProgram.DisplayBoard()

TestAgentProgram.TestingGameOptions()




TestAgentProgram.NextMoveAgent()

TestAgentProgram.AnalyzeSpecificBoard()



