import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

class LogisticRegression:
    
    def  __init__(self, learning_rate=0.001, epochs=100000):
        self._learning_rate = learning_rate
        self._epochs = epochs
        self._weights = None
        self._bias = None

    @property
    def learning_rate(self):
        return self._learning_rate

    @property
    def epochs(self):
        return self._epochs

    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self, weight_list):
        self._weights = weight_list

    @property
    def bias(self):
        return self._bias
    
    @bias.setter
    def bias(self, num):
        self._bias = num


    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
    
        for _ in range(self.epochs):
            linear_predictions = np.dot(X, self.weights) + self.bias
            predictions = sigmoid(linear_predictions)

            dw = (1 / n_samples) * np.dot(X.T, (predictions - y))
            db = (1 / n_samples) * np.sum(predictions - y)

            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate  * db

    
    def predict(self, X):
        linear_pred = np.dot(X, self.weights) + self.bias
        y_pred = sigmoid(linear_pred)
        class_pred = [0 if y<=0.5 else 1 for y in y_pred]
        return class_pred