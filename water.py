from collections import deque

def water_jug_solver():
    # Jug capacities
    capacity_4 = 4
    capacity_3 = 3

    # Initial state
    start = (0, 0)
    
    # To keep track of visited states
    visited = set()
    
    # Queue for BFS: stores (state, path_to_state)
    queue = deque()
    queue.append((start, [start]))

    while queue:
        (x, y), path = queue.popleft()

        # Goal condition
        if x == 2:
            print("Solution path:")
            for step in path:
                print(f"4-gallon: {step[0]}, 3-gallon: {step[1]}")
            return path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # All possible next actions
        next_states = []

        # Fill either jug
        next_states.append((capacity_4, y))  # Fill 4-gallon jug
        next_states.append((x, capacity_3))  # Fill 3-gallon jug

        # Empty either jug
        next_states.append((0, y))  # Empty 4-gallon jug
        next_states.append((x, 0))  # Empty 3-gallon jug

        # Pour from 4 to 3
        pour = min(x, capacity_3 - y)
        next_states.append((x - pour, y + pour))

        # Pour from 3 to 4
        pour = min(y, capacity_4 - x)
        next_states.append((x + pour, y - pour))

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [state]))

    print("No solution found.")
    return None

# Run the solver
water_jug_solver()
