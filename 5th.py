def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == row - i:  # check diagonals
            return False
    return True

def solve(board=[], row=0):
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if is_safe(board, row, col):
            solve(board + [col], row + 1)
def print_board(board):
    for r in range(8):
        row = ""
        for c in range(8):
            if board[r] == c:
                row += " Q "
            else:
                row += " . "
        print(row)
    print("\n" + "-"*32 + "\n")

print("8-Queens Solutions:\n")
solve()
