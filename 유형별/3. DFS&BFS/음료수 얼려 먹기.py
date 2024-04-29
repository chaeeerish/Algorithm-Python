n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]

input_lines = []
for i in range(n):
    line = input()
    input_lines.append(line)

for i in range(n):
    row = [int(char) for char in input_lines[i]]
    graph[i] = row

move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1

        for moving in move:
            dfs(i + moving[0], j + moving[1])
        return True

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1


print(count)

'''
4 5
00110
00011
11111
00000
'''