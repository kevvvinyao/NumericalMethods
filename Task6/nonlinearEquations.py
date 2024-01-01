import math


def f(x1, x2):
    result = x1 - math.cos(x2) - 1
    return result


def g(x1, x2):
    result = x2 - math.sin(x1) - 1
    return result


def phi1(x1, x2):
    result = math.cos(x2) + 1
    return result


def phi2(x1, x2):
    result = math.sin(x1) + 1
    return result


# below is Newton Method's function
def f1(x1, x2):
    result = 1
    return result


def f2(x1, x2):
    result = math.sin(x2)
    return result


def g1(x1, x2):
    result = -math.cos(x1)
    return result


def g2(x1, x2):
    result = 1
    return result


a = 0.26 * math.pi  # 0.8168140899333463
b = 0.27 * math.pi  # 0.8482300164692442
c = 0.55 * math.pi  # 1.7278759594743864
d = 0.56 * math.pi  # 1.7592918860102844
q = 0.99
e = 0.0001
x = (a + b) / 2
y = (c + d) / 2
r = 2 * e
k = 0
while r > e:
    u = x
    v = y
    x = phi1(u, v)
    y = phi2(u, v)
    if x < a or x > b or y < c or y > d:
        print("wrong domain")
        break
    r = abs(x - u)
    s = abs(y - v)
    if s > r:
        r = s
    k = k + 1
    r = r * q / (1 + q)

print("Solution: ")
print(x)
print(y)
print("Times of iteration: ")
print(k)

x = (a + b) / 2
y = (c + d) / 2
r = 2 * e
k = 0
while r > e:
    u = x
    v = y
    s = f1(u, v) * g2(u, v) - f2(u, v) * g1(u, v)
    if s == 0:
        print("det J = 0, wrong")
        break
    x = u - (f(u, v) * g2(u, v) - g(u, v) * f2(u, v)) / s
    y = v - (f1(u, v) * g(u, v) - f(u, v) * g1(u, v)) / s
    r = abs(x - u)
    s = abs(y - v)
    if s > r:
        r = s
    k = k + 1

print("Solution: ")
print(x)
print(y)
print("Times of iteration: ")
print(k)

print("Check the result: ")
print("Substitute the first result = ",end='')
print(f(x, y))
print("Substitute the second result = ", end='')
print(g(x, y))