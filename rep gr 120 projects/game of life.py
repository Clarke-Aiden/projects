import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the game board
board_size = (50, 50)
board = np.zeros(board_size)

# Set up the initial state of the board with random live cells
live_cells = random.sample(list(np.ndindex(board_size)), k=1000)
for i, j in live_cells:
    board[i, j] = 1

# Define the rules for the Game of Life
def update_board(board):
    # Create a new board to hold the updated state
    new_board = np.zeros(board_size)

    # Loop over each cell in the board and apply the rules
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            # Count the number of live neighbors
            num_live_neighbors = np.sum(board[max(0, i-1):min(board_size[0], i+2),
                                               max(0, j-1):min(board_size[1], j+2)]) - board[i, j]

            # Apply the rules
            if board[i, j] == 1 and (num_live_neighbors == 2 or num_live_neighbors == 3):
                new_board[i, j] = 1
            elif board[i, j] == 0 and num_live_neighbors == 3:
                new_board[i, j] = 1

    return new_board

# Define the animation function to update the board at each frame
def animate(frame):
    global board
    board = update_board(board)
    plt.imshow(board, cmap='binary')
    plt.axis('off')

# Set up the animation and show the figure
fig = plt.figure(figsize=(6, 6))
anim = FuncAnimation(fig, animate, frames=100, interval=100)
plt.show()
