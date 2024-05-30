n = int(input())

array = [[] for _ in range(n)]

for i in range(n):
    array[i] = list(map(int, input().split()))

new_array = [[] for _ in range(n)]
new_array[n - 1] = array[n - 1]

for level in range(n - 2, -1, -1):
    for j in range(0, level + 1):
        new_array[level].append(array[level][j] + max(new_array[level + 1][j], new_array[level + 1][j + 1]))

print(new_array[0][0])

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""