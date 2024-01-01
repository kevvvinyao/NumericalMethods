"""
This file contains
Jacobi Rotation Method and
Power Iteration Method
"""
import numpy as np
import math
import myFunction
import copy
n = 3  # dimension of matrix
A = np.loadtxt("1.txt")
OriginA = copy.deepcopy(A)
U = np.zeros((n, n))
UT = np.zeros((n, n))
e = 0.001  # determined accuracy
ep = 0

maxElement = A[0, 1]
maxI = 0
maxJ = 1
for i in range(n):
    for j in range(i + 1, n):
        ep += A[i, j] ** 2
        if abs(A[i, j]) > abs(maxElement):
            maxElement = A[i, j]
            maxI = i
            maxJ = j
ep = ep ** 0.5  # Cycle for both searching for maxElement and calculating ep
phi = 0
k = 0  # times of iteration
V = np.eye(n)
while ep > e:
    if A[maxI, maxI] != A[maxJ, maxJ]:
        phi = 0.5 * math.atan(2 * maxElement / (A[maxI, maxI] - A[maxJ, maxJ]))
    else:
        phi = math.pi / 4
    U[maxI, maxI] = math.cos(phi)
    U[maxJ, maxJ] = math.cos(phi)
    U[maxI, maxJ] = -math.sin(phi)
    U[maxJ, maxI] = math.sin(phi)
    for i in range(n):
        for j in range(n):
            if i == j and i != maxI and j != maxJ:
                U[i, j] = 1
    V = myFunction.matrix_multiply(V, U)
    # UT = np.transpose(U)
    UT = myFunction.matrix_transpose(U)
    A = myFunction.matrix_multiply(UT, A)
    A = myFunction.matrix_multiply(A, U)
    k = k + 1
    U = np.zeros((n, n))
    maxElement = A[0, 1]
    maxI = 0
    maxJ = 1
    ep = 0
    for i in range(n):
        for j in range(i + 1, n):
            ep += A[i, j] ** 2
            if abs(A[i, j]) > abs(maxElement):
                maxElement = A[i, j]
                maxI = i
                maxJ = j
    ep = ep ** 0.5

print("The times of iteration is: ")
print(k)
print("The eigenvalues of matrix A is: ")
for i in range(n):
    print(A[i, i])
print("The eigenvectors of matrix A is: ")
for i in range(n):
    print(V[:, i:i+1])
# for i in range(n):
#     CheckA = copy.deepcopy(OriginA)
#     for j in range(n):
#         CheckA[j, j] = CheckA[j, j] - A[i, i]
#     print(myFunction.matrix_multiply(CheckA, V[:, i:i+1]))

# Check the result: A * x = lambda * x
for i in range(n):
    print("Check the product")
    print(myFunction.matrix_multiply(OriginA, V[:, i:i+1]))
    print(A[i, i] * V[:, i:i+1])

print("Below is power iteration method")
A = copy.deepcopy(OriginA)
y = np.ones((n, 1))
z = myFunction.matrix_multiply(A, y)
for i in range(n):
    if y[i, 0] != 0 and z[i, 0] != 0:
        eigenvalue0 = z[i, 0] / y[i, 0]
        break
y = z / myFunction.vector_modulus(z)
z = myFunction.matrix_multiply(A, y)
for i in range(n):
    if y[i, 0] != 0 and z[i, 0] != 0:
        eigenvalue1 = z[i, 0] / y[i, 0]
        break
y = z / myFunction.vector_modulus(z)
ep = abs(eigenvalue1 - eigenvalue0)
eigenvalue0 = eigenvalue1
k = 2

while ep > e:
    z = myFunction.matrix_multiply(A, y)
    for i in range(n):
        if y[i, 0] != 0 and z[i, 0] != 0:
            eigenvalue1 = z[i, 0] / y[i, 0]
            break
    y = z / myFunction.vector_modulus(z)
    ep = abs(eigenvalue1 - eigenvalue0)
    eigenvalue0 = eigenvalue1
    k = k + 1


print("The times of iteration is: ")
print(k)
print("The spectral radius(max eigenvalue in modulus) is: ")
print(eigenvalue0)
print("The eigenvector with respect to the spectral radius is: ")
print(y)
