def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True


    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player = "X"

for turn in range(9):
    print_board(board)

    print(f"Player {player}'s turn")

    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1

    if 0 <= row < 3 and 0 <= col < 3:

        if board[row][col] == " ":
            board[row][col] = player

            if check_winner(board):
                print("\nFinal Board:\n")
                print_board(board)
                print(f"Player {player} wins!")
                break

            player = "O" if player == "X" else "X"

        else:
            print("Cell already occupied. Try again.")

    else:
        print("Invalid position. Please enter numbers from 1 to 3.")

else:
    print("\nFinal Board:\n")
    print_board(board)
    print("It's a tie!")



#output

"""
  |   |  
---------
  |   |  
---------
  |   |  
---------
Player X's turn
Enter row (1-3): 1
Enter column (1-3): 3
  |   | X
---------
  |   |  
---------
  |   |  
---------
Player O's turn
Enter row (1-3): 2
Enter column (1-3): 2
  |   | X
---------
  | O |  
---------
  |   |  
---------
Player X's turn
...
---------
  |   | X
---------
Player X wins!
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
"""