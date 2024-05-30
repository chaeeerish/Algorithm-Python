def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 경로 압축 적용
    return parent[x]

INF = int(1e9)
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    graph[i][i] = 1

schedules = set(map(int, input().split()))
schedules = [item - 1 for item in schedules]

parent = [INF] * n

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            parent[i] = min(parent[i], j)
print(parent)

filtered = [find_parent(parent, i) for i in range(n) if i in schedules]
if len(set(filtered)) == 1:
    print("YES")
else:
    print("NO")

"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""