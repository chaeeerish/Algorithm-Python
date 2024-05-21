def get_max_profit(cand1, cand2):
    global schedules

    sum1 = 0
    for c in cand1:
        sum1 += schedules[c][1]

    sum2 = 0
    for c in cand2:
        sum2 += schedules[c][1]

    if sum1 > sum2:
        return cand1
    else:
        return cand2


def get_profit(cand):
    global schedules

    sum = 0
    for c in cand:
        sum += schedules[c][1]
    return sum


n = int(input())
schedules = []
for _ in range(n):
    schedules.append(tuple(map(int, input().split())))
schedules.insert(n, (0, 0))

new_schedules = [() for _ in range(len(schedules))]
for i in range(n - 1, -1, -1):
    # 하면
    fixed1 = []
    if schedules[i][0] + i <= n:
        fixed1.append(i)
        j = i + schedules[i][0]
        if j < n:
            fixed1.extend(get_max_profit(new_schedules[j][0], new_schedules[j][1]))

    # 안하면
    fixed2 = []
    if i != n - 1:
        fixed2.extend(get_max_profit(new_schedules[i + 1][0], new_schedules[i + 1][1]))

    # 반영
    new_schedules[i] = (fixed1, fixed2)

print(get_profit(get_max_profit(new_schedules[0][0], new_schedules[0][1])))

"""
# 45
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

# 55
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

# 20
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

# 90
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50

# 101
3
3 100
1 99
1 2

# 1100
4
3 1
1 100
2 100
1 1000

# 105
3
2 100
2 6
1 5

# 20
3
2 10
5 20
1 10

# 3
4
1 1
3 1
1 1
1 1

# 11
5
4 10
2 9
2 3
2 2
3 100

# 10
2
3 100
1 10

# 40
7
3 10
5 20
1 10
2 20
4 15
2 10
2 200

# 161
6
3 20
2 70
3 100
1 40
1 40
1 11

# 16
5
1 6
3 9
3 6
4 9
1 1

# 55
6
1 10
1 10
2 10
1 15
1 10
1 10

# 359
5
1 100
4 200
1 99
2 150
1 160
"""