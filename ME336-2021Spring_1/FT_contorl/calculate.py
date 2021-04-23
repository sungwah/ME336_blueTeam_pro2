import math


def calculate(radius, n, x0, y0):
    x = []
    y = []
    i = 0
    while n > 0:
        x.append(x0 + radius * math.cos(i * 2 * math.pi / n))
        y.append(y0 + radius * math.sin(i * 2 * math.pi / n))
        n = n-1
        i = i+1
    return x, y


if __name__ == '__main__':
    print(calculate(4, 5, 0, 0))
