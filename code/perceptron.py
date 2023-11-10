# Date: Fri Nov 10 16:41:52 2023
# Mail: lunar_ubuntu@qq.com
# Author: https://github.com/xiaoqixian

import numpy as np

class Perceptron:
    def __init__(self):
        self.w = None
        self.b = None

    def train(self, X: np.ndarray, Y: np.ndarray, eta):
        # calculate Gram matrix
        assert X.shape[0] == Y.shape[0]
        w = np.zeros(X.shape[1])
        b = 0

        set_size = X.shape[0]

        complete = False
        while not complete:
            complete = True
            for i in range(set_size):
                if Y[i] * (w.dot(X[i]) + b) <= 0:
                    complete = False
                    w = w + eta * Y[i] * X[i]
                    b = b + eta * Y[i]

        self.w = w
        self.b = b

    def predict(self, x: np.ndarray):
        if not self.w or not self.b:
            return
        return self.w.dot(x) + self.b

    def show(self):
        print("w: ", self.w)
        print("b: ", self.b)

X = np.array([[3,3], [4,3], [1,1]])
Y = np.array([1,1,-1])

perceptron = Perceptron()
perceptron.train(X, Y, 1)
perceptron.show()
