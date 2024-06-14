import numpy as np
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt

#dataset
height = ([150,160,164,165,173]).reshape(-1,1)
weight = np.array([50,65,63,68,72])

#create an linear regression model for the above dataset
model = LinearRegression()

#lets fit the model with approprite data

model.fit(height,weight)


predicted_weight = model.predict(height)

print(f"intercept:{model.intercept_}")
print(f"coeffiecents:{model.coef_[0]}")

#create a scatterplot for above 
plt.scatter(height,weight,color='purple')
plt.plt(height,predicted_weight,color="green")
plt.xlabel('height')
plt.ylabel('weight')
plt.title('linear regression')
plt.show()