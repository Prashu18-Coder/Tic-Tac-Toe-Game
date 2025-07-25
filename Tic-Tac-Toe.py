 # tic tac toe game

def print_board(board):
    count = 0
    for row in board:
        count += 1
        print(" | ".join(row))
        if count < len(board):
            print('-' * 9)
def check_winner(board, player):
    # Rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board , True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board , False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = "O"

def player_move(board):
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            row, col = move // 3, move % 3
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell already taken!")
        except:
            print("Invalid input! Please enter a number from 1 to 9.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe! You are 'X', AI is 'O'")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

play_game()
