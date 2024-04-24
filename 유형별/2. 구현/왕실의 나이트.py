current = input()
x = int(ord(current[0].upper()) - 64)
y = int(current[1])

move = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]

count = 0
for m in move:
    if x + m[0] < 1 or x + m[0] > 8 or y + m[1] < 1 or y + m[1] > 8:
        continue
    count += 1

print(count)