import math

board = [' ' for _ in range(9)]

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print()

def check_winner(board):
    # Winning combinations
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    return None

def is_full(board):
    return ' ' not in board

# Alpha-Beta (Minimax) Algorithm
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:  
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:  
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("Tic-Tac-Toe: You are X, Computer is O")
    print_board(board)

    while True:
        user_move = int(input("Enter your move (1-9): ")) - 1
        if board[user_move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[user_move] = 'X'

        print_board(board)

        if check_winner(board) == 'X':
            print("🎉 You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        print("Computer's turn...")
        move = best_move(board)
        board[move] = 'O'
        print_board(board)

        if check_winner(board) == 'O':
            print("💻 Computer wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

play_game()
