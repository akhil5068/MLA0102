import math

board = [" "]*9

def print_board():
    for i in range(0,9,3):
        print("|".join(board[i:i+3]))
    print()

def winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b1,c in wins:
        if board[a]==board[b1]==board[c]!=" ":
            return board[a]
    return None

def minimax(is_max):
    w = winner(board)
    if w == "O": return 1
    if w == "X": return -1
    if " " not in board: return 0
    best = -math.inf if is_max else math.inf
    for i in range(9):
        if board[i]==" ":
            board[i] = "O" if is_max else "X"
            val = minimax(not is_max)
            board[i] = " "
            best = max(best,val) if is_max else min(best,val)
    return best

def best_move():
    best_val, move = -math.inf, None
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            val=minimax(False)
            board[i]=" "
            if val>best_val:
                best_val,move=val,i
    return move

def play():
    print_board()
    while True:
        move = int(input("Enter your move (0-8): "))
        if board[move]!=" ": continue
        board[move]="X"
        print_board()
        if winner(board) or " " not in board: break
        ai = best_move()
        board[ai]="O"
        print("AI plays:", ai)
        print_board()
        if winner(board) or " " not in board: break
    w = winner(board)
    print("Winner:", w if w else "Draw")

play()
