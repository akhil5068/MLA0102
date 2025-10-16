# Define initial state
state = {
    'monkey': 'A',   # Monkey's position: A, B, or C
    'box': 'B',      # Box's position
    'banana': 'C',   # Banana's position
    'on_box': False  # Is monkey on the box?
}

# Define actions
def move(state, place):
    state['monkey'] = place
    print(f"Monkey moves to {place}")

def push_box(state, place):
    if state['monkey'] == state['box']:
        state['box'] = place
        state['monkey'] = place
        print(f"Monkey pushes box to {place}")

def climb_box(state):
    if state['monkey'] == state['box']:
        state['on_box'] = True
        print("Monkey climbs on the box")

def grab_banana(state):
    if state['monkey'] == state['box'] == state['banana'] and state['on_box']:
        print("Monkey grabs the banana! 🍌")
        return True
    return False

# Simple plan to reach the banana
print("Initial State:", state)
move(state, 'B')
push_box(state, 'C')
climb_box(state)
grab_banana(state)
