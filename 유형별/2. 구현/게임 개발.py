'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

n, m = map(int, input().split())
a, b, d = map(int, input().split())

location = []
for i in range(n):
    location.append(list(map(int, input().split())))

# 0: 북쪽
# 1: 동쪽
# 2: 남쪽
# 3: 서쪽

def rotation(current_d):
    if current_d == 0:
        return 3
    elif current_d == 1:
        return 0
    elif current_d == 2:
        return 1
    elif current_d == 3:
        return 2

def move_front(x, y, current_d):
    if current_d == 0:
        return x - 1, y
    elif current_d == 1:
        return x, y + 1
    elif current_d == 2:
        return x + 1, y
    elif current_d == 3:
        return x, y - 1

def move_back(x, y, current_d):
    if current_d == 0:
        return x + 1, y
    elif current_d == 1:
        return x, y - 1
    elif current_d == 2:
        return x - 1, y
    elif current_d == 3:
        return x, y + 1

block = 1
count = 0
location[a][b] = 1
for i in range(8):
    if count == 3:
        temp = move_back(a, b, d)
        if location[temp[0]][temp[1]] == 1:
            break
        else:
            a = temp[0]
            b = temp[1]
            d = rotation(d)
            location[a][b] = 1
            count = 0
            block += 1

    temp = move_front(a, b, rotation(d))

    if temp[0] < 0 or temp[0] >= n or temp[1] < 0 or temp[1] >= m or location[temp[0]][temp[1]] == 1:
        count += 1
        d = rotation(d)
        continue
    a = temp[0]
    b = temp[1]
    d = rotation(d)
    location[a][b] = 1
    count = 0
    block += 1

print(block)