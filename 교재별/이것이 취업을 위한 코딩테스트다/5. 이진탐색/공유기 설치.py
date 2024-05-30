import sys
input = sys.stdin.readline

N, C = map(int, input().split())
array = [int(input()) for _ in range(N)]
array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1

    for i in range(1, N):
        if array[i] >= value + mid:
            value = array[i]
            count += 1

    if count >= C:
        if result < mid:
            result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

"""
# 3
5 3
1
2
8
4
9

# 2
5 4
1
3
5
10
11

# 3
10 4
1
2
3
4
5
6
7
8
9
10
"""