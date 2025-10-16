puzzle = [[1, 2, 3],
          [4, 0, 6],
          [7, 5, 8]]
def show(p): 
    for r in p: print(*[x if x != 0 else ' ' for x in r])
    print()
def move(p, a, b, x, y):
    p[a][b], p[x][y] = p[x][y], p[a][b]
print("Initial:")
show(puzzle)
move(puzzle, 2, 1, 1, 1)
print("After move:")
show(puzzle)
