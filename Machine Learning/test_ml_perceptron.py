from multi_layer_perceptron import *
from raw_ml_perceptron import *

import numpy as np

# Mock inputs matching slide shapes: 1 sample, 784 features, 10 output classes
np.random.seed(42)
x = np.random.randn(1, 784)
w = np.random.randn(784, 10) * 0.01
b = np.zeros((1, 10))
y = 3  # Target class index

# Instantiate and run execution cycle
model = RawMLPerceptron(x,y)
#or model = MLPerceptron(x,y)
model.creation_architecture([784, 5, 10])
model.forward()
print(f"Initial Cross-Entropy Loss: {model.ce_loss:.4f}")
for i in range(5):
    model.backward()
    #print("Loss:", model.ce_loss)
    #print("p:", model.p)
    #print("delta output:", model.delta[-1])
    #print("delta hidden:", model.delta[0])
    #print("output gradient:",
    #      model.h[-1].T @ model.delta[-1])
    #print("output gradient norm:",
    #      np.linalg.norm(model.h[-1].T @ model.delta[-1]))
    #old_w = model.w_output.copy()

    model.update(learning_rate=0.1)

    #print(
    #    "max weight change:",
    #    np.max(np.abs(model.w_output - old_w))
    #)

    # Forward pass to verify loss decreases
    model.forward()
    print(f"Loss after {i+1} gradient step: {model.ce_loss:.4f}")

