#!/usr/bin/python3
"""Solves the N-queens puzzle"""


import sys


def is_safe(board, row, col):
    """Check if placing a queen at the given position is safe."""
    # Check if there is a queen in the same column or diagonal
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens_util(board, row, n, solutions):
    """Recursively solve the N queens problem."""
    if row == n:
        solutions.append(list(board))
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row] = -1


def solve_n_queens(n):
    """Solve the N queens problem."""
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    """Main function to handle command-line arguments and error checking."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])
