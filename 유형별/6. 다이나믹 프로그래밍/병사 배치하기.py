def get_max_list(cand1, cand2):
    sum1 = sum(cand1)
    sum2 = sum(cand2)

    if sum1 >= sum2:
        return cand1
    else:
        return cand2

n = int(input())
array = list(map(int, input().split()))

dp = [() for _ in range(n)]
dp[n - 1] = ([array[n - 1]], [])

for i in range(n - 2, -1, -1):
    # 포함
    cand1 = []
    if len(dp[i + 1][0]) > 0 and array[i] > dp[i + 1][0][0]:
        cand1 = [array[i]] + dp[i + 1][0]


    cand2 = []
    if len(dp[i + 1][1]) > 0 and array[i] > dp[i + 1][1][0]:
        cand2 = [array[i]] + dp[i + 1][1]

    # 미포함
    cand3 = get_max_list(dp[i + 1][0], dp[i + 1][1])

    # 반영
    dp[i] = (get_max_list(cand1, cand2), cand3)

print(n - len(get_max_list(dp[0][0], dp[0][1])))

"""
# 2
7
15 11 4 8 5 2 4

# 5
12
12 2 5 3 2 10 8 7 15 5 4 3

# 3
4
4 4 4 4 

# 0
1
1000000

# 0
1
1
"""