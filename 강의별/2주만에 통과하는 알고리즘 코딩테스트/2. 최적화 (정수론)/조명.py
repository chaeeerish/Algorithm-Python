n = int(input())
light = [True] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j > n:
            break
        light[i * j] = not light[i * j]

del light[0]

print(light.count(False))