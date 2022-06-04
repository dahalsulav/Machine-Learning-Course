import numpy as np


class LinearRegression:
    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.lr = learning_rate
        self.epochs = n_iters
        self.w = None  # weights
        self.b = None  # bias

    def fit(self, X, y):
        """training and gradient descent

        Args:
            X (_type_): training samples
            y (_type_): respective labels
        """
        # samples and features
        m, n_features = X.shape
        # initializing parameters
        self.w = np.zeros(n_features)
        self.b = 0

        # implementing gradient descent
        for i in range(self.epochs):
            y_pred = np.dot(self.w, X) + self.b
            # calculating gradients i.e. derivatives with respect to parameters

            # X.T means Xi transpose
            dw = (1/(m)) * np.dot(X.T, (y_pred - y))
            db = (1/m) * np.sum(y_pred - y)

            # update weight and bias i.e. w = w - α * dw & b = b - α * db
            self.w -= self.lr * dw
            self.b -= self.lr * dw

    def predict(self, X):
        """ calculate predicted value

        Args:
            X (_type_): test samples

        Returns:
            _type_: predicted value
        """
        # implementing y = w*x + b
        y_pred = np.dot(X, self.w) + self.b
        return y_pred

    # implementing cost function using mean square error
    def mean_square_error(y_pred, y):
        np.mean((y - y_pred) ** 2)


# linear_reg = LinearRegression()
# linear_reg.fit(X_train, y_train)
# y_pred = linear_reg.predict(X_test)
# # calculating error
# meansqrerr = linear_reg.mean_square_error(y_pred, y_test)
# print(meansqrerr)
