"""
This class represents a multi-class Perceptron (Multilayer Perceptron)
model trained via Gradient Descent.
It serves as the foundational architecture for deep neural networks.

@author: Laurie MAVOUNGOU CEO JK AI lmavoungou@outlook.be
@reviewer: Gemini

This version is based on my original implementation and was reviewed
and corrected with the assistance of Google Gemini.
Both versions are kept and presented to document my learning process
and the evolution of the implementation.

"""
import numpy as np


class MLPerceptron:
    def __init__(self, x, y):
        # Ensure input features x is a 2D row vector (1, n_features)
        self.x = np.array(x, dtype=float).reshape(1, -1)
        self.y = int(y)

        self.p = None
        self.ce_loss = None

        self.z = []
        self.h = []
        self.w_hidden = []
        self.b_hidden = []
        self.w_output = None
        self.b_output = None
        self.delta = []
        self.number_of_layers = 0

    def creation_architecture(self, layer_sizes: list):
        self.number_of_layers = len(layer_sizes) - 1

        # Hidden Layers Initialization
        for i in range(len(layer_sizes) - 2):
            W = np.random.randn(layer_sizes[i], layer_sizes[i + 1]) * 0.01
            b = np.zeros((1, layer_sizes[i + 1]))
            self.w_hidden.append(W)
            self.b_hidden.append(b)

        # Output Layer Initialization
        self.w_output = np.random.randn(layer_sizes[-2], layer_sizes[-1]) * 0.01
        self.b_output = np.zeros((1, layer_sizes[-1]))

    def activation(self, z, layer_index):
        if layer_index % 2 == 0:
            return np.maximum(0, z)  # ReLU
        else:
            return np.maximum(np.minimum(z, 1), -1)  # Hard Tanh

    def activation_derivative(self, z, layer_index):
        if layer_index % 2 == 0:
            return (z > 0).astype(float)
        return ((z > -1) & (z < 1)).astype(float)

    def forward(self):
        """
        Logits, Softmax Probabilities, and Cross-Entropy Loss
        """
        self.z = []
        self.h = []

        a = self.x

        # Hidden Layer Forward Pass
        for i, (W, b) in enumerate(zip(self.w_hidden, self.b_hidden)):
            z = np.dot(a, W) + b  # Pre-activation
            self.z.append(z)
            h = self.activation(z, i)  # Activation
            self.h.append(h)
            a = h

        # Output Layer Forward Pass
        L = np.dot(a, self.w_output) + self.b_output  # Logits shape: (1, num_classes)
        self.z.append(L)

        # Numerically Stable Softmax
        L_shifted = L - np.max(L, axis=1, keepdims=True)
        exp_L = np.exp(L_shifted)
        self.p = exp_L / np.sum(exp_L, axis=1, keepdims=True)

        # Categorical Cross-Entropy Loss
        self.ce_loss = -np.log(self.p[0, self.y] + 1e-15)

    def backward(self):
        """
        Backpropagation Signal Calculation
        """
        self.delta = [None] * self.number_of_layers

        # Gradient of Cross-Entropy w.r.t. Logits: dL/dz = p - y
        logit_error = self.p.copy()
        logit_error[0, self.y] -= 1.0
        self.delta[-1] = logit_error

        # Backpropagate through hidden layers
        for u in range(self.number_of_layers - 2, -1, -1):
            if u == self.number_of_layers - 2:
                W = self.w_output
            else:
                W = self.w_hidden[u + 1]

            next_delta = self.delta[u + 1]
            self.delta[u] = np.dot(next_delta, W.T) * self.activation_derivative(self.z[u], u)

        return logit_error

    def update(self, learning_rate):
        """
        Gradient Descent Parameter Update
        """
        # Update Output Layer
        a_last_hidden = self.h[-1] if len(self.h) > 0 else self.x
        self.w_output -= learning_rate * np.dot(a_last_hidden.T, self.delta[-1])
        self.b_output -= learning_rate * self.delta[-1]

        # Update Hidden Layers
        for u in range(self.number_of_layers - 2, -1, -1):
            a_previous = self.x if u == 0 else self.h[u - 1]
            self.w_hidden[u] -= learning_rate * np.dot(a_previous.T, self.delta[u])
            self.b_hidden[u] -= learning_rate * self.delta[u]