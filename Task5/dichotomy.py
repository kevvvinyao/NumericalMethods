import math


def origin_f(x):
    result = math.sin(x) - 2 * (x ** 2) + 0.5
    return result


def derivative_f(x):
    result = math.cos(x) - 4 * x
    return result


def iteration_f(x):  # phi(x)
    result = math.sqrt(0.5 * (math.sin(x) + 0.5))
    return result


e = 10 ** -3  # 10 ^ (-3)
l = 0
r = 0
# find the positive root
while origin_f(l) * origin_f(r) > 0:
    r = r + 0.2

Right_end = r
Left_end = Right_end - 0.2
l = Left_end
k = 0
ep = abs(0.5 * (l - r))
while ep > e:
    m = 0.5 * (l + r)
    if origin_f(m) * origin_f(l) > 0:
        l = m
    else:
        r = m
    ep = abs(0.5 * (l - r))
    k = k + 1
solution = 0.5 * (l + r)
print("The solution of Dichotomy method: ")
print(solution)
print("The times of iteration: ")
print(k)
# above is dichotomy
# below is fixed-point iteration method
l = Left_end
r = Right_end
x0 = (l + r) / 2
x1 = 0
ep = abs(0.5 * (l - r))
q = 0.26
k = 0
while ep > e:
    x1 = iteration_f(x0)
    ep = q / (1 - q) * (x1 - x0)
    x0 = x1
    k = k + 1

print("The solution of fixed-point iteration: ")
print(x1)
print("The times of iteration: ")
print(k)
# below is Newton method
# print("We choose Right_end as the initial approximation, and prove its convergence:")
# print(derivative_second_f(0.8) * origin_f(0.8), end='')
# print(" > 0")
x0 = Right_end
x1 = 0
ep = abs(0.5 * (l - r))
k = 0
while ep > e:
    x1 = x0 - origin_f(x0) / derivative_f(x0)
    ep = x1 - x0
    x0 = x1
    k = k + 1

print("The solution of Newton method: ")
print(x1)
print("The times of iteration: ")
print(k)

x0 = Left_end
x1 = Right_end
ep = abs(0.5 * (l - r))
x2 = 0
k = 0
while ep > e:
    a = origin_f(x1) - origin_f(x0)
    b = origin_f(x1) * (x1 - x0)
    x2 = x1 - b / a
    ep = abs(x2 - x1)
    x0 = x1
    x1 = x2
    k = k + 1

print("The solution of secant method: ")
print(x2)
print("The times of iteration: ")
print(k)

print("Substitute the result to check: ")
print(origin_f(x2))
