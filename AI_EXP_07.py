
def print_board(board):
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):
    # All queens have been placed
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'

            if solve(board, row + 1, n):
                return True

            # Backtracking
            board[row][col] = '.'

    return False


# Main program
n = 8
board = [['.' for _ in range(n)] for _ in range(n)]

if solve(board, 0, n):
    print("Solution for the 8 Queens Problem:")
    print_board(board)
else:
    print("No solution found.")



#output
""" Solution for the 8 Queens Problem:
Q . . . . . . .
. . . . Q . . .
. . . . . . Q .
. . . . . Q . .
. . Q . . . . .
. . . . . . . Q
. Q . . . . . .
. . . Q . . . ."""