import math, random

# (a) Represent the board
EMPTY, HUMAN, AI = '.', 'h', 'a'
board = [
    [AI, '.', AI, '.', AI, '.', AI, '.'],
    ['.', AI, '.', AI, '.', AI, '.', AI],
    [AI, '.', AI, '.', AI, '.', AI, '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', HUMAN, '.', HUMAN, '.', HUMAN, '.', HUMAN],
    [HUMAN, '.', HUMAN, '.', HUMAN, '.', HUMAN, '.'],
    ['.', HUMAN, '.', HUMAN, '.', HUMAN, '.', HUMAN],
]

# Display board
def show(b):
    for r in b: print(' '.join(r))
    print()

# Get all possible moves for a player (simplified)
def get_moves(b, player):
    moves = []
    for i in range(8):
        for j in range(8):
            if b[i][j] == player:
                dirs = [(-1, -1), (-1, 1)] if player == AI else [(1, -1), (1, 1)]
                for d in dirs:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < 8 and 0 <= nj < 8 and b[ni][nj] == EMPTY:
                        new_b = [row[:] for row in b]
                        new_b[ni][nj], new_b[i][j] = player, EMPTY
                        moves.append(new_b)
    return moves

# Evaluate board (simple heuristic)
def evaluate(b):
    return sum(r.count(AI) - r.count(HUMAN) for r in b)

# (c) Minimax with Alpha–Beta pruning
def minimax(b, depth, alpha, beta, maximizing):
    if depth == 0:
        return evaluate(b), b
    moves = get_moves(b, AI if maximizing else HUMAN)
    if not moves:
        return evaluate(b), b
    best_move = None
    if maximizing:
        max_eval = -math.inf
        for m in moves:
            eval, _ = minimax(m, depth-1, alpha, beta, False)
            if eval > max_eval:
                max_eval, best_move = eval, m
            alpha = max(alpha, eval)
            if beta <= alpha: break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for m in moves:
            eval, _ = minimax(m, depth-1, alpha, beta, True)
            if eval < min_eval:
                min_eval, best_move = eval, m
            beta = min(beta, eval)
            if beta <= alpha: break
        return min_eval, best_move

# (b, d) Play game loop (Human vs AI)
turn = HUMAN
while True:
    show(board)
    if not get_moves(board, turn):
        print("Winner:", "AI" if turn == HUMAN else "Human")
        break
    if turn == HUMAN:
        i, j, ni, nj = map(int, input("Enter move i j ni nj: ").split())
        if board[i][j] == HUMAN and board[ni][nj] == EMPTY:
            board[ni][nj], board[i][j] = HUMAN, EMPTY
            turn = AI
    else:
        print("AI thinking...")
        _, board = minimax(board, 3, -math.inf, math.inf, True)
        turn = HUMAN
