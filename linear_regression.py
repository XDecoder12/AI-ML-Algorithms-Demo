import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])

model = LinearRegression()
model.fit(x,y)

prediction = model.predict([[10]])

print("Prediction for x=10:", prediction[0])
print("Coefficient (a):", model.coef_[0])
print("Intercept (b):", model.intercept_)