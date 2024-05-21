import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))


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