# Function to check if a queen can be placed at grid[x][y]
def is_safe(grid, x, y, n):
    # Check the column for any queen
    for row in range(x):
        if grid[row][y] == 1:
            return False
    
    # Check upper left diagonal for any queen
    row, col = x, y
    while row >= 0 and col >= 0:
        if grid[row][col] == 1:
            return False
        row -= 1
        col -= 1
    
    # Check upper right diagonal for any queen
    row, col = x, y
    while row >= 0 and col < n:
        if grid[row][col] == 1:
            return False
        row -= 1
        col += 1
    
    return True

# Function to print the board configuration
def print_board(grid, n):
    for i in range(n):
        for j in range(n):
            print("Q" if grid[i][j] == 1 else ".", end=" ")
        print()

# Backtracking function to solve N-Queens problem
def solve_nqueens_util(grid, x, n):
    # If all queens are placed, return True
    if x >= n:
        print_board(grid, n)
        print("\n")
        return True
    
    # Try to place the queen in all columns one by one
    for y in range(n):
        if is_safe(grid, x, y, n):
            grid[x][y] = 1  # Place the queen
            
            # Recursively place queens in the next row
            if solve_nqueens_util(grid, x + 1, n):
                return True  # If placing queen leads to a solution, return True

            # If placing queen doesn't lead to a solution, backtrack
            grid[x][y] = 0  # Remove the queen (backtrack)

    return False  # If no position is found for the queen, return False

# Function to solve the N-Queens problem
def solve_nqueens():
    n = int(input("Enter the size of the board (N): "))  # Size of the board
    grid = [[0 for _ in range(n)] for _ in range(n)]  # Initialize an empty grid
    
    if not solve_nqueens_util(grid, 0, n):
        print("No solution exists")

if __name__ == "__main__":
    solve_nqueens()
