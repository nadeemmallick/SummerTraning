import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt


#TASKS 1


#Question 1

Engine_size = np.array([800,1000,1200,1500,1800])
Price_lakhs = np.array([3,4.5,5.5,7,9])
Engine_array = Engine_size.reshape(-1,1)
print(Engine_array)

#Question 2

model = LinearRegression()
model.fit(Engine_array, Price_lakhs)

#Question 3

print(model.predict([[1100],[1600],[2000]]))


#Question 4

plt.scatter(Engine_size, Price_lakhs, marker='o')
plt.grid(True)
plt.show()

#Question 5

m, b = np.polyfit(Engine_size, Price_lakhs,1)
regression_line = m * Engine_size + b
plt.scatter(Engine_size, Price_lakhs, label='Data Points')
plt.plot(Engine_size, regression_line,color='red', label='Regression Line')
plt.legend()
plt.grid(True)
plt.show()

#Question 6

plt.plot(Engine_size, Price_lakhs,label='Unpredicted price')
plt.scatter(Engine_array, Price_lakhs, marker='x',color='red',linewidths=3,label='Predicted price')
plt.grid(True)
plt.legend()
plt.show()


#TASKS 2

house_size = np.array([500, 750, 1000, 1250, 1500])
house_price = np.array([100, 200, 300, 400, 500])
reshaped_size = house_size.reshape(-1, 1)

#Question 1
model = LinearRegression()
model.fit(reshaped_size, house_price)

#Question 2
price=model.predict(np.array([[2000],[3000],[4000],[5000],[7500]]))
print(price)

#Question 3
plt.scatter(house_size, house_price, marker='o', color='red',label='Actual Data')
plt.legend()
plt.grid(True)
plt.show()

#Question 4
M,B = np.polyfit(house_size, house_price, deg=1)
Regression_line = M * house_size + B
plt.plot(house_size, Regression_line, color='blue',label='Regression Line')
plt.legend()
plt.grid(True)
plt.show()

#Question 5
plt.plot(house_size, house_price, color='blue',label='Actual Data')
plt.scatter(reshaped_size, house_price, marker='o', color='red',label='Predicted Data')
plt.legend()
plt.grid(True)
plt.show()


