import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
# random.seed(40)
# np.random.seed(40)
X_train = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y_train = np.array([45000, 50000, 60000, 80000, 110000, 150000, 200000, 300000, 500000, 1000000])
poly_model = PolynomialFeatures(degree=2)
model = LinearRegression()
scaler = StandardScaler()
X_train_poly = poly_model.fit_transform(X_train)
model.fit(X_train_poly, y_train)
plt.scatter(X_train, y_train, c='r')
def computeCost(X, y, w, b):
    m = X.shape[0]
    cost = 0.0
    for i in range(m):
        f_wb_i = np.dot(X[i], w) + b
        cost += (f_wb_i - y[i]) ** 2
    cost/=(2*m)
    return cost

def computeGrad(X, y, w, b):
    m,n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.0
    for i in range(m):
        error = np.dot(X[i], w) + b - y[i]
        for j in range(n):
            dj_dw[j] += error * X[i,j]
        dj_db += error
    dj_db /= m
    dj_dw /= m
    return dj_dw, dj_db

def gradientDescent(X, y, w, b, alpha, iterations):
    m = X.shape[0]
    for i in range(iterations):
        dj_dw, dj_db = computeGrad(X, y, w, b)
        w -= alpha * dj_dw
        b -= alpha * dj_db
    return w, b

w_init = np.zeros((X_train.shape[1],))
b_init = 0.0
w_final, b_final = gradientDescent(X_train, y_train, w_init, b_init, 5.0e-7, 1000)
print("Final w:", w_final)
print("Final b:", b_final)
