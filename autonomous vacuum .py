import random

# Create grid (0 = clean, 1 = dirty)
grid = [[random.choice([0, 1]) for _ in range(5)] for _ in range(5)]

def print_grid():
    for row in grid:
        print(row)
    print()

# Vacuum starting position
x, y = 0, 0

def clean_all():
    global x, y
    moves = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            x, y = i, j
            if grid[x][y] == 1:
                grid[x][y] = 0
                print(f"Cleaned cell ({x},{y})")
            moves += 1
            print_grid()
    print(f"All cells clean! Total moves: {moves}")

print("Initial grid:")
print_grid()
clean_all()
