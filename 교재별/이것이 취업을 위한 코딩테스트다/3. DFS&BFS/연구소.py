import itertools, copy, math
from collections import deque

n, m = map(int, input().split()) # n: 행 m: 열
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

def get_candidate(graph):
    global n, m
    array = set()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                array.add((i, j))

    return array

def infect(graph, virus_array):
    for virus in virus_array:
        queue = deque([virus])
        while queue:
            v = queue.popleft()
            udrl = [(v[0] + 1, v[1]), (v[0] - 1, v[1]), (v[0], v[1] - 1), (v[0], v[1] + 1)]
            for x, y in udrl:
                if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
                    graph[x][y] = 2
                    queue.append((x, y))

    return graph

def get_safe_area(graph):
    global n, m

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1

    if count == 0:
        return -1
    return count

virus_array = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus_array.append((i, j))

candidate = get_candidate(graph)

max_area = -1
for elec in itertools.combinations(candidate, 3):
    infected_graph = copy.deepcopy(graph)
    for e in elec:
        infected_graph[e[0]][e[1]] = 1
    infected_graph = infect(infected_graph, virus_array)
    max_area = max(max_area, get_safe_area(infected_graph))

print(max_area)

"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""