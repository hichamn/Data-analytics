# Python code to perform linear regression on a dataset

import numpy as np
from sklearn.linear_model import LinearRegression

# Sample dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])

# Create a linear regression object
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict the y values for new x values
y_pred = model.predict(X)

# Print the slope and y-intercept of the regression line
print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)

# Print the predicted y values
print("Predicted y values: ", y_pred)
