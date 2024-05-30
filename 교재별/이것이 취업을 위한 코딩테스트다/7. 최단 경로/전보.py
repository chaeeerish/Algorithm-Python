"""
3 2 1
1 2 4
1 3 2
"""
import heapq

INF = int(1e9)

n, m, c = map(int, input().split()) # 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

count = 0

def dijkstra(start):
    global count
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q) # dist: 1과 node가 연결된 거리
        if distance[node] < dist:
            continue
        else:
            for i in graph[node]:
                cost = dist + i[1] # i[0]: node와 그래프의 다른 점이 연결된 거리
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
                    count = count + 1

dijkstra(c)

for i in range(n+1):
    if distance[i] == INF:
        distance[i] = 0

print(count, max(distance))

