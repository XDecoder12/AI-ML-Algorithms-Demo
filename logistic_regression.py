import numpy as np
from sklearn.linear_model import LogisticRegression

x = np.array([[10],[13],[16],[19],[24],[30]]) #number of hours studied
y = np.array([1,0,0,0,1,1]) # pass(1) or fail(0)

model = LogisticRegression()
model.fit(x,y)

prediction = model.predict([[20]])
probability = model.predict_proba([[20]])

print("Prediction of the model (0=Fail and 1=Pass): ", prediction[0])
print("Probability: ", probability)