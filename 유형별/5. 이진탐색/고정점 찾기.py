n = int(input())
array = list(map(int, input().split()))

start = 0
end = len(array) - 1

flag = 0
while start <= end:
    mid = (start + end) // 2
    if array[start] == start:
        print(start)
        flag = 1
        break
    elif array[end] == end:
        print(end)
        flag = 1
        break
    elif array[mid] == mid:
        print(mid)
        flag = 1
        break

    if array[mid] > mid:
        end = mid - 1
    elif array[mid] < mid:
        start = mid + 1

if flag == 0:
    print(-1)

"""
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
"""