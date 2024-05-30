import math

n = int(input())
array = list(map(int, input().split()))

array.sort()

home = [0] * (array[-1] + 1)

for i in range(n):
    home[array[i]] += 1

sum = math.inf
antenna = 0
for i in range(1, len(home)):
    temp_sum = 0
    for j in range(1, len(home)):
        temp_sum += abs(i - j) * home[j]
    if temp_sum < sum:
        sum = temp_sum
        antenna = i

print(antenna)

"""
4
5 1 7 9
"""