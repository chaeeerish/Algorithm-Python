import copy
import itertools

def search_direction(hall, t, d_row, d_col):
    row, col = t[0], t[1]
    while True:
        row += d_row
        col += d_col
        if row < 0 or row >= len(hall) or col < 0 or col >= len(hall) or hall[row][col] == 'O' or hall[row][col] == 'T':
            break
        elif hall[row][col] == 'S':
            return False
        elif hall[row][col] == 'X':
            continue
    return True

def observe(hall, teacher):
    cnt = 0
    udrl = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for t in teacher:
        for d_row, d_col in udrl:
            if not search_direction(hall, t, d_row, d_col):
                return False
    return True

n = int(input())
hall = []
for _ in range(n):
    hall.append(list(map(str, input().split())))

blank = []
teacher = []
student_cnt = 0
for i in range(n):
    for j in range(n):
        if hall[i][j] == 'X':
            blank.append((i, j))
        elif hall[i][j] == 'T':
            teacher.append((i, j))
        elif hall[i][j] == 'S':
            student_cnt += 1

flag = "NO"
for hurdle in itertools.combinations(blank, 3):
    hall_copy = copy.deepcopy(hall)
    for x,  y in hurdle:
        hall_copy[x][y] = 'O'
    if observe(hall_copy, teacher):
        flag = "YES"
        break

print(flag)



"""
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

4
S S S T
X X X X
X X X X
T T T X
"""