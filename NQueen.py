def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[row][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[row][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, solutions):
    if col >= len(board):
        solutions[0] += 1
        print_board(board)
        print()  # Print a blank line between solutions
        return False  # Change to False to find all solutions

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1, solutions):
                return True

            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = [0]  # Use a list to allow updates within solve_n_queens_util

    solve_n_queens_util(board, 0, solutions)

    print(f"Number of possible solutions: {solutions[0]}")
    return solutions[0] > 0

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))

# Example usage
n = 8
solve_n_queens(n)
