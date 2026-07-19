import pandas as pd
import matplotlib.pyplot as plt

df  = pd.read_csv('LinerRegression/salary_data.csv')

# Traning Phase

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=0)

"""
LinearRegression
Definition : LinearRegression(*, fit_intercept=True, copy_X=True, tol=1e-6, n_jobs=None, positive=False)

Ordinary least squares Linear Regression.

LinearRegression fits a linear model with coefficients w = (w1, ..., wp) to minimize the residual sum of squares between the observed targets in the dataset, and the targets predicted by the linear approximation.
"""

from sklearn.linear_model import LinearRegression # LinearRegression is Algorithem
regressor = LinearRegression() # regressor is model
regressor.fit(x_train, y_train)


# Testing Phase
y_pred = regressor.predict(x_test)
print(y_pred) # it can compare with the y_test

comparison = pd.DataFrame({
    'Actual': y_test,
    'Predicated':y_pred
})
print(comparison)

plt.scatter(x_test, y_test, color='red')
plt.plot(x_train,regressor.predict(x_train),color="blue")
plt.title("Salary VS Experience (Test set)")
plt.xlabel("Years Of Experience")
plt.ylabel("Salary")
plt.show()

# Validation Phase : Y^ = mx+c

m = regressor.coef_
print(m)

c = regressor.intercept_
print(c)

y_12 = (m * 12) + c # 12 year Experience
print(y_12)
y_20 = (m * 20) + c # 20 year Experience
print(y_20)
  
