import math
import numpy as np


def f(t):
    # result = math.log(t) * t
    result = math.atan(t)
    return result


def ff(t):
    # result = t ** 2 / 4 * (2 * math.log(t) - 1)
    result = math.atan(t) * t - 0.5 * math.log(t ** 2 + 1)
    return result


n = 5
with open('h.txt', 'r') as file:
    data = file.read()
h = float(data)
x = np.loadtxt("nodes.txt")
x_m = np.zeros(len(x) - 1)
for i in range(n - 1):
    x_m[i] = (x[i] + x[i + 1]) / 2
y = np.zeros(len(x))
for i in range(n):
    y[i] = f(x[i])
y_m = np.zeros(len(x) - 1)
for i in range(n - 1):
    y_m[i] = f(x_m[i])
# Calculate the exact value
I = ff(x[4]) - ff(x[0])
print("The exact value of integral: ", end='')
print(I)

# Calculate the left-point method
I_l = 0
for i in range(n - 1):
    I_l += h * y[i]
print("The left-point method: ", end='')
print(I_l)
print("Error: ", end='')
print(abs(I - I_l))

# Calculate the right-point method
I_r = 0
for i in range(1, n):
    I_r += h * y[i]
print("The right-point method: ", end='')
print(I_r)
print("Error: ", end='')
print(abs(I - I_r))

# Calculate the mid-point method
I_m = 0
for i in range(n - 1):
    I_m += h * y_m[i]
print("The mid-point method: ", end='')
print(I_m)
print("Error: ", end='')
print(abs(I - I_m))

# Trapezoid rule
I_t = 0
for i in range(n - 1):
    I_t += 0.5 * h * (y[i] + y[i + 1])
print("The trapezoid method: ", end='')
print(I_t)
print("Error: ", end='')
print(abs(I - I_t))

# Simpson's rule
I_s = 0
for i in range(n - 1):
    I_s += h / 6 * (y[i] + 4 * y_m[i] + y[i + 1])
print("The Simpson's method: ", end='')
print(I_s)
print("Error: ", end='')
print(abs(I - I_s))

# Below is RRR method to refine
print()
print("RRR method to refine: ")
p = 2  # The order of accuracy
m = 2
n_interval = n - 1
Ith = I_t
print("The result of 1h step trapezoid: ", end='')
print(Ith)
print("Error: ", end='')
print(abs(I - Ith))
It2h = 2 * h / 2 * (y[0] + 2 * y[2] + y[4])
print("The result of 2h step trapezoid: ", end='')
print(It2h)
print("Error: ", end='')
print(abs(I - It2h))
It4h = 4 * h / 2 * (y[0] + y[4])
print("The result of 4h step trapezoid: ", end='')
print(It4h)
print("Error: ", end='')
print(abs(I - It4h))
q = p + math.log(n_interval) / math.log(m)

# first refine
print("Below is the 1st refinement: ")
Ith1r = Ith + (Ith - It2h) / (m ** p - 1)
print("The result of 1h step 1st refine: ", end='')
print(Ith1r)
print("Error: ", end='')
print(abs(I - Ith1r))
It2h1r = It2h + (It2h - It4h) / (m ** p - 1)
print("The result of 2h step 1st refine: ", end='')
print(It2h1r)
print("Error: ", end='')
print(abs(I - It2h1r))

# second refine
print("Below is the 2nd refinement: ")
p = 3
Ith2r = Ith1r + (Ith1r - It2h1r) / (m ** p - 1)
print("The result of 1h step 2nd refine: ", end='')
print(Ith2r)
print("Error: ", end='')
print(abs(I - Ith2r))
