def direction(m, c):
    if m == 'L':
        return left(c)
    elif m == 'R':
        return right(c)
    elif m == 'U':
        return up(c)
    elif m == 'D':
        return down(c)

def left(c):
    return (c[0], c[1] - 1)

def right(c):
    return (c[0], c[1] + 1)

def up(c):
    return (c[0] - 1, c[1])

def down(c):
    return (c[0] + 1, c[1])

#
n = int(input())
move = list(input().split())

current = (1, 1)

for m in move:
    temp = direction(m, current)
    if temp[0] > n or temp[0] < 1 or temp[1] > n or temp[1] < 1:
        continue
    else:
        current = direction(m, current)

print(current)

