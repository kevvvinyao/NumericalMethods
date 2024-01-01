import numpy as np
import copy
import myFunction
n = 4  # the number of equations
e = 0.01  # determined accuracy
C = np.loadtxt("10.txt")  # read data from file
d = C[:, n]  # d is the right-hand side
C = C[:, :n]  # C is updated to be coefficient matrix
a = np.zeros((n, n))
b = np.zeros((n, 1))
x = np.zeros((n, 1))
y = np.zeros((n, 1))

for i in range(n):  # i is from 0 to (n-1) not including n
    b[i] = d[i] / C[i, i]
    for j in range(n):
        if i != j:
            a[i, j] = -C[i, j] / C[i, i]
        else:
            a[i, j] = 0
x = copy.deepcopy(b)  # the first time of iteration
y = copy.deepcopy(x)  # y is to store the previous time of solution

# normA = np.linalg.norm(a, np.inf)
normA = 0
for i in range(n):
    normAtmp = 0  # A is n * n matrix
    for j in range(n):
        normAtmp = normAtmp + abs(a[i, j])
    if normAtmp > normA:
        normA = normAtmp
q = normA

if normA >= 1:  # make sure convergence (sufficient condition)
    print("The convergence condition is not fulfilled!")

normX = 0
for i in range(n):
    if abs(x[i]) > normX:
        normX = abs(x[i])

# ep = q / (1 - q) * np.linalg.norm(x, np.inf)
ep = q / (1 - q) * normX

t = 0
while ep > e:
    y = copy.deepcopy(x)
    x = myFunction.matrix_multiply(a, y) + b
    # ep = q / (1 - q) * np.linalg.norm((x - y), np.inf)
    XY = x - y  # XY is (n * 1) vector
    normXY = 0
    for i in range(n):
        if abs(XY[i]) > normXY:
            normXY = abs(XY[i])
    ep = q / (1 - q) * normXY
    t = t + 1

print("The result of fixed-point iterative method is: ")
print(x)
print("The times of iteration is: ")
print(t)

# below is Seidel method
x = copy.deepcopy(b)
y = copy.deepcopy(x)
normX = 0
for i in range(n):
    if abs(x[i]) > normX:
        normX = abs(x[i])

# ep = q / (1 - q) * np.linalg.norm(x, np.inf)
ep = q / (1 - q) * normX

t = 0
while ep > e:
    y = copy.deepcopy(x)
    for i in range(n):
        x[i] = myFunction.vector_multiply(a[i, :], x) + b[i]
    # ep = q / (1 - q) * np.linalg.norm((x - y), np.inf)
    XY = x - y  # XY is (n * 1) vector
    normXY = 0
    for i in range(n):
        if abs(XY[i]) > normXY:
            normXY = abs(XY[i])
    ep = q / (1 - q) * normXY
    t = t + 1

print("The result of Seidel iterative method is: ")
print(x)
print("The times of iteration is: ")
print(t)
