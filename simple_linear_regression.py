import numpy as np

# Generate a small dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Simple linear regression model
class LinearRegression:
    def __init__(self):
        self.slope = 0
        self.intercept = 0

    def fit(self, X, y):
        n = len(X)
        mean_x = np.mean(X)
        mean_y = np.mean(y)

        numerator = 0
        denominator = 0

        for i in range(n):
            numerator += (X[i] - mean_x) * (y[i] - mean_y)
            denominator += (X[i] - mean_x) ** 2

        self.slope = numerator / denominator
        self.intercept = mean_y - (self.slope * mean_x)

    def predict(self, X):
        return self.slope * X + self.intercept

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make a prediction
new_X = np.array([[6]])
prediction = model.predict(new_X)

print(f"Prediction for X=6: {prediction}")
