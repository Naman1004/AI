def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, col, n):
    # Base case: If all queens are placed
    if col >= n:
        return True
    
    # Try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place queen
            
            # Recur to place rest of the queens
            if solve_nqueens_util(board, col + 1, n):
                return True
            
            board[i][col] = 0  # Backtrack if no solution found
    
    return False

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    
    if not solve_nqueens_util(board, 0, n):
        print("No solution exists")
        return False
    
    # Print the solution
    for row in board:
        print(row)
    
    return True

# Example usage
n = 8  # Number of queens (for 8-queens problem)
solve_nqueens(n)
