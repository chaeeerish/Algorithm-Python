INF = int(1e9)
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distances = [INF] * (n + 1)
visited = [False] * (n + 1)

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distances[i] < min_value and not visited[i]:
            min_value = distances[i]
            index = i

    return index

def dijkstra():
    distances[1] = 0
    visited[1] = True
    for i in graph[1]:
        distances[i] = 1

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distances[now] + 1
            if cost < distances[j]:
                distances[j] = cost

dijkstra()

distances[0] = 0
max_distance = max(distances)
hide_barn = distances.index(max_distance)
barn_count = distances.count(max_distance)

print(hide_barn, max_distance, barn_count)

"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""