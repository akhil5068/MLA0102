import random

def cost(state):
    attacks = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_neighbors(state):
    neighbors = []
    n = len(state)
    for c in range(n):
        for r in range(n):
            if r != state[c]:
                neighbor = state.copy()
                neighbor[c] = r
                neighbors.append(neighbor)
    return neighbors

def hill_climb(state):
    while True:
        neighbors = get_neighbors(state)
        costs = [cost(n) for n in neighbors]
        min_cost = min(costs)
        if min_cost >= cost(state):
            return state
        state = neighbors[costs.index(min_cost)]

def solve_n_queens(n, restarts=10):
    best_state = None
    best_cost = float('inf')
    for _ in range(restarts):
        state = [random.randint(0, n - 1) for _ in range(n)]
        result = hill_climb(state)
        c = cost(result)
        if c < best_cost:
            best_state, best_cost = result, c
        if best_cost == 0:
            break
    return best_state, best_cost

# Run
n = 8
final_state, final_cost = solve_n_queens(n)
print("Final State:", final_state)
print("Final Cost:", final_cost)
print("Solution Found!" if final_cost == 0 else "Local Optimum Reached.")
