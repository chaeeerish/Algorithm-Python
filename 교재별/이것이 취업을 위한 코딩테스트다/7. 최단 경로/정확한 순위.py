INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(0, n + 1):
    for b in range(0, n + 1):
        if graph[a][b] == INF:
            graph[a][b] = 0

cnt = 0
for i in range(1, n + 1):
    if sum(graph[i]) + sum([row[i] for row in graph]) == n:
        cnt += 1
print(cnt)

#
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if graph[a][b] == INF:
#             print(0, end="\t")
#         else:
#             print(graph[a][b], end="\t")
#     print()

"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""