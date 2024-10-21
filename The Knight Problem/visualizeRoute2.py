import tkinter as tk
from tkinter import messagebox #provides pop-up message dialogue

chessboard_size = 8
chessboard = [[0 for _ in range(chessboard_size)] for _ in range(chessboard_size)]
solution = [[0 for _ in range(chessboard_size)] for _ in range(chessboard_size)]

# Initialize the knight & its 8 legal possible moves on the chessboard
move_row = [2, 1, -1, -2, -2, -1, 1, 2]
move_col = [1, 2, 2, 1, -1, -2, -2, -1]


def get_possible(row, col):
    possible_moves = []
    for i in range(8):  # only 8 possible moves
        if 0 <= row + move_row[i] < chessboard_size and 0 <= col + move_col[i] < chessboard_size and \
                chessboard[row + move_row[i]][col + move_col[i]] == 0:
            possible_moves.append((row + move_row[i], col + move_col[i]))
    return possible_moves


def solve(x, y, step):
    countSteps = 1
    chessboard[x][y] = countSteps  # Set the starting square to 1
    while countSteps < chessboard_size ** 2:
        position = get_possible(x, y)
        min_moves = float('inf')
        next_move = None
        for p in position:
            moves = len(get_possible(p[0], p[1]))
            if moves < min_moves:
                min_moves = moves
                next_move = p
        x, y = next_move
        countSteps += 1
        chessboard[x][y] = countSteps
        step += 1
        yield next_move

# draw chessboard on the tkinter canvas
def draw_board(board):
    for row in range(chessboard_size):
        for col in range(chessboard_size):
            color = "white" if (row + col) % 2 == 0 else "blue"
            canvas.create_rectangle(col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, fill=color)
            step = board[row][col]
            if step > 0:  # Check if step is greater than 0 to display the number
                canvas.create_text(col * 50 + 25, row * 50 + 25, text=str(step), font=("Arial", 16)) #display the step number on the square.


def next_step(): #to provide animation of the steps on the tkinter canvas
    global step, route, solution
    try:
        next_move = next(route) 
        row, col = next_move
        solution[row][col] = step + 1
        draw_board(solution) #updates the canvas with the current state of the chessboard
        step += 1
        root.after(500, next_step)  # Automate next step after 200 milliseconds (adjust as needed)
    except StopIteration: #means the squares are complete
        messagebox.showinfo("Route Complete", "Knight's tour completed successfully!")


def create_route(): #intialize knight's tour based on the user input
    global step, route, solution
    x = int(entry_x.get()) #to get the user input row
    y = int(entry_y.get()) #to get the user input column
    step = 0  # Start from 0 instead of 1
    route = solve(x, y, step)
    next_step() #starts the tour and visualization
    entry_x.config(state=tk.DISABLED) #disables further input from the user
    entry_y.config(state=tk.DISABLED)


# Create GUI
root = tk.Tk()
root.title("Knight's Tour Warnsdorf")

# Calculate position to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 800
window_height = 600
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT)

canvas = tk.Canvas(frame_left, width=400, height=400)
canvas.pack()

frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT)

label_x = tk.Label(frame_right, text="Enter starting row (0-7):")
label_x.grid(row=0, column=0, padx=8, pady=8)

entry_x = tk.Entry(frame_right)
entry_x.grid(row=0, column=1, padx=8, pady=8)

label_y = tk.Label(frame_right, text="Enter starting column (0-7):")
label_y.grid(row=1, column=0, padx=8, pady=8)

entry_y = tk.Entry(frame_right)
entry_y.grid(row=1, column=1, padx=8, pady=8)

button_create_route = tk.Button(frame_right, text="Create Route", command=create_route)
button_create_route.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
