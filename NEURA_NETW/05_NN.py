import numpy as np

np.random.seed(0)

X = [[1, 2, 3, 2.5],
     [2, 5, -1, 2],
     [-1.5, 2.7, 3.3, -.8]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = .1*np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
