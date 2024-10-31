a, b, c, d, e, f = map(int, input().split())

for x in range(-10000, 10001):
    for y in range(-10000, 10001):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)