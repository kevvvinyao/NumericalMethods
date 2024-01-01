import numpy as np
import math


def f(x):
    # result = math.log(x)
    result = math.atan(x)
    return result


x_star = -0.5
u = x_star
real_value = f(u)
n = 6
x = np.loadtxt("u.txt")
y = np.zeros(x.shape)
a = np.zeros(len(x) - 1)
b = np.zeros(len(x) - 1)
c = np.zeros(len(x) - 1)
d = np.zeros(len(x) - 1)
p = np.zeros(len(x) - 2)
q = np.zeros(len(x) - 2)


for i in range(n):
    y[i] = f(x[i])

for i in range(n - 1):
    a[i] = y[i]


c[0] = 0
p[0] = -(x[2] - x[1]) / (2 * x[2] - 2 * x[0])
q[0] = 3 * ((y[2] - y[1]) / (x[2] - x[1]) - (y[1] - y[0]) / (x[1] - x[0])) / (2 * x[2] - 2 * x[0])
for i in range(1, n - 2):
    p[i] = -(x[i + 2] - x[i + 1]) / ((2 * x[i + 2] - 2 * x[i]) + (x[i + 1] - x[i]) * p[i - 1])
    q[i] = (3 * ((y[i + 2] - y[i + 1]) / (x[i + 2] - x[i + 1]) - (y[i + 1] - y[i]) / (x[i + 1] - x[i])) \
            - (x[i + 1] - x[i]) * q[i - 1]) / ((2 * x[i + 2] - 2 * x[i]) + (x[i + 1] - x[i]) * p[i - 1])
c[n - 2] = q[n - 3]
for i in range(n - 3, 0, -1):
    c[i] = p[i - 1] * c[i + 1] + q[i - 1]

# below is to calculate coefficient b and d
for i in range(n - 2):
    b[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i]) - (x[i + 1] - x[i]) * (c[i + 1] + 2 * c[i]) / 3
    d[i] = (c[i + 1] - c[i]) / (x[i + 1] - x[i]) / 3
b[n - 2] = (y[n - 1] - y[n - 2]) / (x[n - 1] - x[n - 2]) - (x[n - 1] - x[n - 2]) * 2 * c[n - 2] / 3
d[n - 2] = -c[n - 2] / (x[n - 1] - x[n - 2]) / 3

# find where is x_star
j = 0
for i in range(n - 1):
    if x[i] <= u <= x[i + 1]:
        j = i


u = u - x[j]
v = a[j] + b[j] * u + c[j] * u ** 2 + d[j] * u ** 3

print("The result of Cubic Spline: ")
print("The real value is: ", end='')
print(real_value)
print("The approximation value is: ", end='')
print(v)
print("The error between them is: ", end='')
print(abs(v - real_value))

# below is the least square method
# 1st degree
m = 2
a = np.zeros((m, m))
b = np.zeros(m)
c = np.zeros(m)
for i in range(m):
    for j in range(m):
        for k in range(n):
            a[i, j] = a[i, j] + x[k] ** (i + j)

for i in range(m):
    for j in range(n):
        b[i] = b[i] + y[j] * (x[j] ** i)

# m == 2 solve the equations by Cramer method
g = a[0, 0] * a[1, 1] - a[1, 0] * a[0, 1]
c[0] = (b[0] * a[1, 1] - b[1] * a[1, 0]) / g
c[1] = (a[0, 0] * b[1] - a[1, 0] * b[0]) / g
print("The coefficient of 1st degree least square: ")
print(c[0], c[1])
e = 0
for i in range(n):
    e += ((c[0] + c[1] * x[i]) - f(x[i])) ** 2
print("The error of 1st degree: ")
print(e)

# 2 nd degree
m = 3
a = np.zeros((m, m))
b = np.zeros(m)
c = np.zeros(m)
for i in range(m):
    for j in range(m):
        for k in range(n):
            a[i, j] = a[i, j] + x[k] ** (i + j)

for i in range(m):
    for j in range(n):
        b[i] = b[i] + y[j] * (x[j] ** i)
# m == 3 solve the equations by Cramer Rule
g = a[0, 0] * a[1, 1] * a[2, 2] + a[1, 0] * a[2, 1] * a[0, 2] + \
    a[2, 0] * a[0, 1] * a[1, 2] - a[2, 0] * a[1, 1] * a[0, 2] - \
    a[0, 0] * a[2, 1] * a[1, 2] - a[1, 0] * a[0, 1] * a[2, 2]
c[0] = (b[0] * a[1, 1] * a[2, 2] + b[1] * a[2, 1] * a[0, 2] + b[2] * a[0, 1] * a[1, 2] -\
        b[2] * a[1, 1] * a[0, 2] - b[0] * a[2, 1] * a[1, 2] - b[1] * a[0, 1] * a[2, 2]) / g
c[1] = (a[0, 0] * b[1] * a[2, 2] + a[1, 0] * b[2] * a[0, 2] + a[2, 0] * b[0] * a[1, 2] -\
        a[2, 0] * b[1] * a[0, 2] - a[0, 0] * b[2] * a[1, 2] - a[1, 0] * b[0] * a[2, 2]) / g
c[2] = (a[0, 0] * a[1, 1] * b[2] + a[1, 0] * a[2, 1] * b[0] + a[2, 0] * a[0, 1] * b[1] -\
        a[2, 0] * a[1, 1] * b[0] - a[0, 0] * a[2, 1] * b[1] - a[1, 0] * a[0, 1] * b[2]) / g
print("The coefficient of 2nd degree least square: ")
print(c[0], c[1], c[2])
e = 0
for i in range(n):
    e += ((c[0] + c[1] * x[i] + c[2] * (x[i] ** 2)) - f(x[i])) ** 2
print("The error of 2nd degree: ")
print(e)
