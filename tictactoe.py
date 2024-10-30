import math
board = [' ' for _ in range(9)] #initialize

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def is_moves_left(board):
    return ' ' in board
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]             # Diagonals
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

def evaluate(board):
    if check_winner(board, 'O'):  # AI is 'O'
        return 10
    elif check_winner(board, 'X'):  # Human is 'X'
        return -10
    else:
        return 0
def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)
    
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    # Maximizer (AI's move)
    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(board, depth + 1, False, alpha, beta))
                board[i] = ' '
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best

    # Minimizer (Human's move)
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(board, depth + 1, True, alpha, beta))
                board[i] = ' '
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best
def find_best_move(board):
    best_val = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move
def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    print_board()

    while True:
        # Human's turn
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] == ' ':
            board[human_move] = 'X'
        else:
            print("Invalid move. Try again.")
            continue

        print_board()
        if check_winner(board, 'X'):
            print("Congratulations, you win!")
            break
        elif not is_moves_left(board):
            print("It's a draw!")
            break
        print("AI is making its move...")
        ai_move = find_best_move(board)
        board[ai_move] = 'O'
        print_board()
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif not is_moves_left(board):
            print("It's a draw!")
            break
play_game()
