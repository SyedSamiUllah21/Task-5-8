PLAYER_X, PLAYER_O, EMPTY = "X", "O", " "

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    return None

def minimax(board, is_max):
    winner = check_winner(board)
    if winner == PLAYER_X: return 1
    if winner == PLAYER_O: return -1
    if EMPTY not in board: return 0

    best = float('-inf') if is_max else float('inf')
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X if is_max else PLAYER_O
            score = minimax(board, not is_max)
            board[i] = EMPTY
            best = max(best, score) if is_max else min(best, score)
    return best

def find_best_move(board, is_max):
    best_move, best_score = None, float('-inf') if is_max else float('inf')
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X if is_max else PLAYER_O
            score = minimax(board, not is_max)
            board[i] = EMPTY
            if (is_max and score > best_score) or (not is_max and score < best_score):
                best_score, best_move = score, i
    return best_move

board = [PLAYER_X, PLAYER_O, PLAYER_X, PLAYER_O, PLAYER_X, EMPTY, EMPTY, PLAYER_O, EMPTY]
best_move = find_best_move(board, True)  
print(f"Best move for player X: {best_move}")
