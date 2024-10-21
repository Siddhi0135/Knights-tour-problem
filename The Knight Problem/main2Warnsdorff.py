chessboard_size = 8
chessboard = [[0 for i in range(chessboard_size)] for i in range(chessboard_size)]

# Initialize the knight & its 8 legal possible moves on the chessboard
move_row = [2, 1, -1, -2, -2, -1, 1, 2]
move_col = [1, 2, 2, 1, -1, -2, -2, -1]


def printKnightRoute():
    # this function will print the Route of the Knight on a chessboard[8][8]
    for i in range(chessboard_size):
        for j in range(chessboard_size):
            print('{:2d}'.format(chessboard[i][j]), end=' ') #2d for proper alignment of the text
        print()


def get_possible(row, col): #for all possible moves of knight from its current position
    possible_moves = [] 
    for i in range(8):  
        if row + move_row[i] >= 0 and row + move_row[i] < chessboard_size and col + move_col[i] >= 0 and col + move_col[
            i] < chessboard_size and chessboard[row + move_row[i]][col + move_col[i]] == 0: #the last condition checks whether the knight has visited the square destination or not
            possible_moves.append([row + move_row[i], col + move_col[i]]) 
    return possible_moves 


def solve(x, y): #solve the knight's tour using warnsdorff's heuristic. starts from position (x,y).
    countSteps = 1 
    chessboard[x][y] = countSteps
    while countSteps < chessboard_size ** 2:
        position = get_possible(x, y) 
        min_moves = float('inf') #initialized with greater value to find the move that has the fewest onwards move
        next_move = None
        # Warnsdorff's Rule: The knight should move to the square from which it has the fewest onward moves. This helps to prevent the knight from getting stuck.
        for p in position: 
            moves = len(get_possible(p[0], p[1])) #count how many moves are available from the current position.
            if moves < min_moves: 
                min_moves = moves
                next_move = p
        x, y = next_move 
        countSteps += 1 
        chessboard[x][y] = countSteps 

#main function to execute knight's tour
if __name__ == "__main__":
    start_x = int(input("Enter starting row (1-8): ")) - 1
    start_y = int(input("Enter starting column (1-8): ")) - 1
    solve(start_x, start_y)
    printKnightRoute()
