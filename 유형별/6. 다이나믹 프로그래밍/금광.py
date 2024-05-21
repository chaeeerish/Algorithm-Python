import copy

def get_value(x, y):
    global golds_dp, n, m
    if 0 <= x < n and 0 <= y < m:
        return golds_dp[x][y]
    return -1

T = int(input())

answers = []
for _ in range(T):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    a = 0
    golds = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            golds[i].append(array[a])
            a += 1

    golds_dp = [[0] * m for _ in range(n)]
    for i in range(n):
        golds_dp[i][0] = golds[i][0]

    maximum = -1
    for j in range(1, m):
        for i in range(0, n):
            golds_dp[i][j] = golds[i][j] + max(get_value(i - 1, j - 1), get_value(i, j - 1), get_value(i + 1, j - 1))
            if j == m - 1:
                maximum = max(maximum, golds_dp[i][j])

    answers.append(maximum)

for answer in answers:
    print(answer)

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""