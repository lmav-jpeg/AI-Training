"""
This class represent multi-class Perceptron model trained
via Gradient Descent (or Softmax/Multinomial Logistic Regression).
It serves as the foundational output layer for deep neural networks

@author: Laurie MAVOUNGOU CEO JK AI lmavoungou@outlook.be

Tip from gpt
            L_shifted = L - np.max(L)
            sum_exp = np.sum(np.exp(L_shifted))
            self.p = np.exp(L_shifted) / sum_exp
"""
import numpy as np

class Perceptron:
    def __init__(self,x,w,b,y):
        self.x = x
        self.w = w
        self.b = b
        self.p = None
        self.ce_loss = None
        self.y = y


    def forward(self):
        '''
        Logits, Softmax Probabilities and Cross-Entropy Loss
        :return: None
        '''
        # Logits (L): Linear layer output
        L = (np.dot(self.x,self.w) + self.b).flatten()

        # Activation layer
        self.p = np.zeros(L.shape)
        sum_exp = np.sum(np.exp(L))
        for i in range (self.p.shape[0]):
           self.p[i] = np.exp(L[i]) / sum_exp

        self.ce_loss = - np.log(self.p[self.y])


    def backward(self):
        """
        Vectorized Gradient Signal
        :return: logit_error
        """
        logit_error = np.zeros(self.p.shape)

        # Populate element by element across all classes
        for j in range(self.p.shape[0]):
            if j == self.y:
                logit_error[j] = self.p[j] - 1.0
            else:
                logit_error[j] = self.p[j]

        return logit_error

    def update(self, learning_rate):
        '''
        Weight Update and Bias Update
        :param learning_rate:
        :return:None
        '''
        logit_error = self.backward().reshape(1,-1)
        self.w = self.w - learning_rate *  self.x.T.dot(logit_error)
        self.b = self.b - learning_rate * logit_error



