import math
import numpy as np


def f(x):
    result = math.atan(x)
    return result


u = -0.5
n = 4  # number of nodes
x = np.loadtxt("1.txt")
y = np.zeros(x.shape)
for i in range(n):
    y[i] = f(x[i])
solution = 0
for i in range(n):
    v = y[i]
    for j in range(n):
        if i != j:
            v = v * (u - x[j]) / (x[i] - x[j])
    solution += v
print("The real result: ", end='')
print(f(u))
print("The result of Lagrange Method: ", end='')
print(solution)
print("The error: ", end='')
print(abs(solution - f(u)))

a = np.zeros((len(x), len(x)))
for i in range(n):
    a[i][0] = y[i]
# for i in range(n - 1):
#     a[i][1] = (a[i][0] - a[i + 1][0]) / (x[i] - x[i + 1])
# for i in range(n - 2):
#     a[i][2] = (a[i][1] - a[i + 1][1]) / (x[i] - x[i + 2])
# for i in range(n - 3):
#     a[i][3] = (a[i][2] - a[i + 1][2]) / (x[i] - x[i + 3])
for j in range(1, n):
    for i in range(n - j):
        a[i][j] = (a[i][j - 1] - a[i + 1][j - 1]) / (x[i] - x[i + j])

solution = 0
for i in range(n):
    v = a[0][i]
    for j in range(i):
        v = v * (u - x[j])
    solution = solution + v

print("The result of Newton Method: ", end='')
print(solution)
print("The error: ", end='')
print(abs(solution - f(u)))
