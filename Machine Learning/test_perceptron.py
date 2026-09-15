from perceptron import *

import numpy as np

# Mock inputs matching slide shapes: 1 sample, 784 features, 10 output classes
np.random.seed(42)
x = np.random.randn(1, 784)
w = np.random.randn(784, 10) * 0.01
b = np.zeros((1, 10))
y = 3  # Target class index

# Instantiate and run execution cycle
model = Perceptron(x, w, b, y)
model.forward()
print(f"Initial Cross-Entropy Loss: {model.ce_loss:.4f}")
for i in range(10):
    model.update(learning_rate=0.01)

    # Forward pass to verify loss decreases
    model.forward()
    print(f"Loss after {i+1} gradient step: {model.ce_loss:.4f}")