"""
This class represent my original multi-class Perceptron model trained
via Gradient Descent (or Softmax/Multinomial Logistic Regression).
It serves as the foundational output layer for deep neural networks

@author: Laurie MAVOUNGOU CEO JK AI lmavoungou@outlook.be

This code presents bugs on:
- explicit 2D input handling;
- 2D output representation;
- vectorized softmax;
- output-layer handling;
- initialization;
- update logic;
- separation between forward/backward/update.
"""
import numpy as np

class RawMLPerceptron:
    def __init__(self,x,y):
        self.x = x
        self.p = None
        self.ce_loss = None
        self.y = y
        self.z = []
        self.h = []
        self.w_hidden = []
        self.b_hidden = []
        self.delta = []

    def creation_architecture(self, layer_sizes: list):
        self.number_of_layers = len(layer_sizes) -1
        for i in range(len(layer_sizes) - 2):
            W = np.random.randn(
                layer_sizes[i],
                layer_sizes[i + 1]
            ) * 0.01

            b = np.zeros(layer_sizes[i + 1])

            self.w_hidden.append(W)
            self.b_hidden.append(b)

        # Output layer
        self.w_output = np.random.randn(
            layer_sizes[-2],
            layer_sizes[-1]
        ) * 0.01

        self.b_output = np.zeros(layer_sizes[-1])

    def activation(self, z, layer_index):
        if layer_index%2 == 0:
            return np.maximum(0, z)
        else:
            return np.maximum(np.minimum(z, 1), -1)

    def activation_derivative(self, z, layer_index):
        if layer_index % 2 == 0:
            return (z > 0).astype(float)

        return ((z > -1) & (z < 1)).astype(float)


    def forward(self):
        '''
        Logits, Softmax Probabilities and Cross-Entropy Loss
        :return: None
        '''
        self.z = []
        self.h = []

        #Hidden Layers forwarding
        a = self.x

        for i, (W, b) in enumerate (zip(self.w_hidden, self.b_hidden)):
            z = np.dot(a, W) + b # Logits (L): Linear layer output/pre-activation values
            self.z.append(z)
            h = self.activation(z,i)

            self.h.append(h)

            a = h

        # Logits (L): Linear layer output/pre-activation values
        L = np.dot(a, self.w_output) + self.b_output
        # Activation layer
        self.z.append(L)
        L_shifted = L - np.max(L) #Tip to handle large number
        self.p = np.zeros(L_shifted.shape)
        sum_exp = np.sum(np.exp(L_shifted))
        for i in range (self.p.shape[0]):
           self.p[i] = np.exp(L_shifted[i]) / sum_exp #post activation values

        self.ce_loss = - np.log(self.p[self.y])


    def backward(self):
        """
        Vectorized Gradient Signal
        :return: logit_error
        """

        self.delta = [None] * self.number_of_layers

        # Output error: p - y
        logit_error = np.zeros(self.p.shape)

        # Populate element by element across all classes
        for j in range(self.p.shape[0]):
            if j == self.y:
                logit_error[j] = self.p[j] - 1.0
            else:
                logit_error[j] = self.p[j]

        self.delta[-1] = logit_error

        for u in range(self.number_of_layers - 2, -1, -1):
            if u == self.number_of_layers - 2:
                # From output layer → last hidden layer
                next_delta = self.delta[u + 1]
                W = self.w_output
            else:
                # From hidden layer → previous hidden layer
                next_delta = self.delta[u + 1]
                W = self.w_hidden[u + 1]

            self.delta[u] = next_delta @ W.T * self.activation_derivative(self.z[u], u)
        return logit_error

    def update(self, learning_rate):
        '''
        Weight Update and Bias Update
        :param learning_rate:
        :return:None
        '''

        for u in range(self.number_of_layers - 2, -1, -1):
            if u == self.number_of_layers - 2:
                self.w_output -= learning_rate * self.h[-1].T.dot(self.delta[-1])
                self.b_output -= learning_rate * self.delta[-1]
            else:
                if u == 0:
                    a_previous = self.x
                else:
                    a_previous = self.h[u - 1]
                self.w_hidden[u] -= learning_rate * a_previous.T.dot(self.delta[u])
                self.b_hidden [u] -= learning_rate * self.delta[u]


