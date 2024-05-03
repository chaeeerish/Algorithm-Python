"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
curriculum = [{}]
indegree = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    curriculum.append({i})
    for d in data[1:]:
        if d == -1:
            break
        else:
            graph[d].append(i)
            indegree[i] += 1

def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            curriculum[i].update(curriculum[now])

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        result = 0
        for c in curriculum[i]:
            result += time[c]
        print(result)

topology_sort()