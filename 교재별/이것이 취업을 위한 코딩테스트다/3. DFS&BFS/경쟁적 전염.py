n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())
x = x - 1
y = y - 1

def infect(graph, virus):
    virus_coordinate = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == virus:
                virus_coordinate.append((i, j))

    for v in virus_coordinate:
        udrl = [(v[0] + 1, v[1]), (v[0] - 1, v[1]), (v[0], v[1] + 1), (v[0], v[1] - 1)]
        for i, j in udrl:
            if 0 <= i < n and 0 <= j < n and graph[i][j] == 0:
                graph[i][j] = virus

    return graph

for time in range(s):
    for virus in range(1, k + 1):
        graph = infect(graph, virus)
        print(graph)

print(graph[x][y])

"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2
"""