import math
def sigmoid(x): return 1 / (1 + math.exp(-x))
def relu(x): return max(0, x)

def dot(a, b): return sum(x*y for x, y in zip(a, b))

data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]
w1 = [[5, 5], [-5, -5]] 
b1 = [-2.5, 7.5]
w2 = [7, 7]  
b2 = -6
def forward(x):

    h = []
    for i in range(2):
        z = dot(w1[i], x) + b1[i]
        h.append(relu(z))  # ReLU activation

    # Output layer
    out = sigmoid(dot(w2, h) + b2)  # Sigmoid activation
    return out

# Test on XOR dataset
for x, y in data:
    output = forward(x)
    print(f"Input: {x}, Predicted: {round(output, 3)}, Expected: {y}")
