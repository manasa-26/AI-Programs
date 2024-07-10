board = [[' ' for x in range(3)] for y in range(3)]

def display_board():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = " ")
        print()

def check_winner():
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def play():
    while True:
        display_board()
        player = "X"
        while True:
            try:
                row = int(input("Enter row for player " + player + ": "))
                col = int(input("Enter col for player " + player + ": "))
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if board[row][col] == ' ':
                        board[row][col] = player
                        break
                    else:
                        print("Position already filled. Try again.")
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")
        winner = check_winner()
        if winner:
            display_board()
            print("Player " + winner + " wins!")
            break
        player = "O" if player == "X" else "X"

play()
