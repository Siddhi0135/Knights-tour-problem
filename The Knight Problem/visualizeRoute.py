import tkinter as tk #used to create GUI in python

chessboard_size = 8


move_row = [2, 1, -1, -2, -2, -1, 1, 2]
move_col = [1, 2, 2, 1, -1, -2, -2, -1]


def isValidKnightTour(row, col, chessboard):
    
    if 0 <= row < chessboard_size and 0 <= col < chessboard_size and chessboard[row][col] == -1:
        return True
    return False

#solveKnightTourBacktracking() attempts to solve the knight's tour using backtracking, updating both the chessboard data and the Tkinter canvas for visualization.
#canvas: Tkinter canvas where the tour is visually drawn.
def solveKnightTourBacktracking(current_row, current_col, move_row, move_col, counterKnightSteps, chessboard, canvas):
    if counterKnightSteps == chessboard_size ** 2: #check if all steps are completed
        return True

    # Try all the next moves from the current row and col
    for i in range(8):
        new_move_row = current_row + move_row[i]
        new_move_col = current_col + move_col[i]
        if isValidKnightTour(new_move_row, new_move_col, chessboard):
            chessboard[new_move_row][new_move_col] = counterKnightSteps
            canvas.create_text(new_move_col * 50 + 25, new_move_row * 50 + 25, text=str(counterKnightSteps),
                               fill="black", font=("Arial", 12, "bold")) # Draws the current step number at the new position
            canvas.update()  # Update the canvas to show the change

            if solveKnightTourBacktracking(new_move_row, new_move_col, move_row, move_col, counterKnightSteps + 1,
                                           chessboard, canvas): #recursively call itself to attempt to solve the knight's tour
                return True #if solution is found return true.

            # Backtracking :if current moves leads to dead end that is no further valid move the algorithm backtracks
            canvas.create_rectangle(new_move_col * 50, new_move_row * 50, (new_move_col + 1) * 50,
                                     (new_move_row + 1) * 50, fill="white") #revert the last move visually by redrawing the square as white
            chessboard[new_move_row][new_move_col] = -1 #marks the square as unvisited
            canvas.update()  # Update the canvas to show the change

    return False #if no valid move return false.


def KnightTourMain():
    # Initialize the chessboard
    chessboard = [[-1 for _ in range(chessboard_size)] for _ in range(chessboard_size)]
    chessboard[0][0] = 0 #sets first square as visited

    # Create a Tkinter window
    root = tk.Tk() #create main window of GUI
    root.title("Knight's Tour Backtracking") 

    # Create a canvas to draw the chessboard and knight's tour
    canvas = tk.Canvas(root, width=chessboard_size * 50, height=chessboard_size * 50) 
    canvas.pack()

    # Draw the chessboard
    for i in range(chessboard_size):
        for j in range(chessboard_size):
            color = "white" if (i + j) % 2 == 0 else "blue"
            canvas.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill=color)

    # Start the knight's tour
    solveKnightTourBacktracking(0, 0, move_row, move_col, 1, chessboard, canvas)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    KnightTourMain()
