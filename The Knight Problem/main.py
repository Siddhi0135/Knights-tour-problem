# The code is divided into different files to improve code organization, modularity, and maintainability.
# 
#  Initialize the chessboard and it's size
chessboard_size = 8 #size of chessboard
chessboard = [[-1 for i in range(chessboard_size)] for i in range(chessboard_size)] #initialize each entry by -1.

# Initialize the knight & it's 8 legal possible moves on the chessboard
move_row = [2, 1, -1, -2, -2, -1, 1, 2]
move_col = [1, 2, 2, 1, -1, -2, -2, -1]


def isValidKnightTour(row, col):
    # this function checks if the position[row][col] of the knight is valid inside our chessboard
    if row >= 0 and row >= 0 and row < chessboard_size and col < chessboard_size and chessboard[row][col] == -1: #to check that knight remains in the bound
        return True
    return False


def printKnightRoute():
    # this function will print the Route of the Knight on a chessboard[8][8]
    for i in range(chessboard_size):
        for j in range(chessboard_size):
            print('{:2d}'.format(chessboard[i][j]), end=' ')
        print()

#uf knight reaches 64 it means it has visited all the cells in the board and return true
def solveKnightTourBacktracking(current_row, current_col, move_row, move_col, counterKnightSteps):
    if counterKnightSteps == chessboard_size ** 2:
        return True

    # Try all the next moves from the current row and col
    for i in range(8):
        new_move_row = current_row + move_row[i]
        new_move_col = current_col + move_col[i]
        if isValidKnightTour(new_move_row, new_move_col):
            chessboard[new_move_row][new_move_col] = counterKnightSteps
            if solveKnightTourBacktracking(new_move_row, new_move_col, move_row, move_col, counterKnightSteps + 1):
                return True

            # If the knight reaches a position where no valid further moves are possible, the function undoes the current move by resetting the square to -1, allowing it to try a different move.
            chessboard[new_move_row][new_move_col] = -1
    return False #no valid path return false


def KnightTourMain():
    # This uses the function KnightTourBacktracking:
    # either it returns false if no complete tour is possible
    # or it returns true and prints the tour on the chessboard

    chessboard[0][0] = 0 #initial position of knight

    counterKnightSteps = 1 #keeps track of how many move the knight makes

    # Checking if solution exists or not
    if not solveKnightTourBacktracking(0, 0, move_row, move_col, counterKnightSteps):
        print("Solution doesn't exist")
    else:
        printKnightRoute()


if __name__ == "__main__":

    KnightTourMain()
