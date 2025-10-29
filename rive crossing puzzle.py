from collections import deque

def is_valid(state):
    M_left, C_left, boat = state
    M_right, C_right = 3 - M_left, 3 - C_left
    if (M_left < C_left and M_left > 0) or (M_right < C_right and M_right > 0):
        return False
    return 0 <= M_left <= 3 and 0 <= C_left <= 3

def successors(state):
    M_left, C_left, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    next_states = []
    for m, c in moves:
        if boat == 1:  # boat on left
            new_state = (M_left - m, C_left - c, 0)
        else:          # boat on right
            new_state = (M_left + m, C_left + c, 1)
        if is_valid(new_state):
            next_states.append(new_state)
    return next_states

def solve():
    start, goal = (3, 3, 1), (0, 0, 0)
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        state = path[-1]
        if state == goal:
            return path
        for next_state in successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(path + [next_state])

solution = solve()
for step in solution:
    print(step)
