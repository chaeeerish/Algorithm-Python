# 시간복잡도: O(logN)
from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
array = list(map(int, input().split()))

r_i = bisect_right(array, x)
l_i = bisect_left(array, x)

if r_i - l_i == 0:
    print(-1)
else:
    print(r_i - l_i)

"""
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
"""