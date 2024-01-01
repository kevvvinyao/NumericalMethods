import numpy as np
import math


def f(f_x):
    result = math.atan(f_x)
    # result = math.log(f_x)
    # result = math.log(f_x) * f_x
    # result = math.cos(f_x) / math.sin(f_x) + f_x
    return result


def d_f(f_x):
    result = 1 / (f_x ** 2 + 1)
    # result = 1 / f_x
    # result = math.log(f_x) + 1
    # result = -1 / (math.sin(f_x) ** 2) + 1
    return result


def dd_f(f_x):
    result = -2 * f_x / ((f_x ** 2 + 1) ** 2)
    # result = -1 / (f_x ** 2)
    # result = 1 / f_x
    # result = math.sin(2 * f_x) / (math.sin(f_x) ** 4)
    return result


n = 5
with open('u.txt', 'r') as file:
    data = file.read()
u = float(data)

x = np.loadtxt("nodes.txt")
y = np.zeros(len(x))
d = np.zeros((n, n))

for i in range(n):
    y[i] = f(x[i])

for i in range(n):
    d[i, 0] = y[i]
for i in range(1, n):  # from the second column
    for j in range(n - i):  # the rows
        d[j, i] = (d[j, i - 1] - d[j + 1, i - 1]) / (x[j] - x[i + j])
# first derivative
solution = 0
for i in range(1, n):  # i is from 1
    f = 0
    for j in range(i):
        g = d[0, i]
        for k in range(i):
            if j != k:
                g *= (u - x[k])
        f += g
    solution += f
print("Below is the 1st derivative: ")
print("The approximate result: ", end='')
print(solution)
print("The exact result: ", end='')
print(d_f(u))
print("error = ", end='')
print(abs(solution - d_f(u)))

# Below is the 2nd derivative
solution = 0
f = 0
for i in range(3, n):
    for j in range(i):
        for k in range(i):
            g = d[0, i]  # reset g after updating k
            trigger = 0
            for m in range(i):  # 最小遍历单位
                if j != k and j != m and k != m:
                    g *= (u - x[m])
                    trigger = 1
            if trigger == 1:  # update final result before changing k
                f += g
f = f + d[0, 2] * 2
print("Below is the 2nd derivative: ")
print("The approximate result: ", end='')
print(f)
print("The exact result: ", end='')
print(dd_f(u))
print("error = ", end='')
print(abs(f - dd_f(u)))
