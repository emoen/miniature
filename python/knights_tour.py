from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, U, V, visited, move, knight_move, path, adj, n, m, longest_path')

n, m = 8, 8  # Define the chessboard size (8x8 for a standard chessboard)
knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]  # Define all valid knight moves

# Create adjacency list for knight moves
for x in range(n):
    for y in range(m):
        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                +adj((x, y), (nx, ny))

# Define the path rules
path(X, Y) <= adj(X, Y) & ~visited(Y)
path(X, Y) <= adj(Y, X) & ~visited(X)

# Ensure each cell is visited exactly once
visited(X) <= path(U, X) & (U != X)
visited(X) <= path(X, U) & (U != X)

# Ensure that the knight does not start and stop at the same cell
pyDatalog.create_terms('start, end')
start(X) <= ~visited(X) & (X == (0, 0))  # Start at the top-left corner (0, 0)
end(X) <= ~visited(X) & (X != (0, 0))    # End at any other cell

# Track the longest path found
longest_path = [0]  # Use a mutable object to track the longest path length

# Query to find the knight's tour
print("asking")
result = pyDatalog.ask('path(X, Y)')
print(result)
