import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

height=np.array([150,160,164,170,174]).reshape(-1,1)
weight=np.array([50,40,30,60,70])

#create a linear regression madal
modal=LinearRegression()
#lets fit the modal
modal.fit(height,weight)

predict_weight=modal.predict(height)


print(f"intercept: {modal.intercept_}")
print(f"coeffient: {modal.coef_[0]}")



plt.scatter(height,weight, color='blue',label='Testing Data')
plt.plot(height,weight, color='hotpink',label='Regression Line')
plt.title('simple regression')
plt.xlabel('height')
plt.ylabel('weight')
plt.legend()
plt.show()