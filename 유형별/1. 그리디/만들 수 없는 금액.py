"""
5
3 2 1 1 9
"""
n = int(input())
array = list(map(int, input().split()))
array.sort()

target = 1
for x in array:
    if target < x:
        break
    target += x

print(target)