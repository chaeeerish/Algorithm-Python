## 최단 경로
### 가장 빠른 길 찾기
- 최단 경로 알고리즘은 말그대로 가장 짧은 경로를 찾는 알고리즘이다.
- '한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우', '모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야 하는 경우' 등의 다양한 사례가 존재한다.
- 최단 경로 문제는 보통 그래프를 이용해 표현한다.
- 보통 자주 사용하는 알고리즘은 다음과 같다.
  - 다익스트라 최단 경로 알고리즘
  - 플로이드 워셜 알고리즘
  - 벨만 포드 알고리즘

### 다익스트라 최단 경로 알고리즘
- **특정한 노드**에서 출발하여 **다른 노드로 가는** 각각의 최단 경로를 구해주는 알고리즘이다.
- 매번 '가장 비용이 적은 노드'를 선택해서 과정을 반복한다.
  - 출발 노드를 설정한다.
  - 최단 거리 테이블을 초기화한다.
  - **방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.**
  - 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
- 간단하게 다익스트라 알고리즘을 구현하는 방법을 알아보자.
  - 노드의 개수를 V라 할 때, O(V^2)의 시간 복잡도를 가진다.
```python
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
  
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
      if distance[i] < min_value and not visited[i]:
        min_value = distance[i]
        index = i
        
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
```

- 개선된 다익스트라 알고리즘을 구현하는 방법을 알아보자.
  - 최악의 경우에도 O(ElogV)를 보장하여 해결할 수 있다.
  - 개선된 다익스트라 알고리즘에서는 힙 자료구조를 사용한다.
> 힙 자료구조는 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나이다.
> 대부분의 프로그래밍 언어에서는 우선순위 큐 라이브러리를 지원하기 때문에 직접 힙 자료구조부터 작성할 일은 없다.
> 파이썬에서는 PriorityQueue와 heapq를 지원하지만, heapq가 더 빠르게 동작한다.

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
```

### 플로이드 워셜 알고리즘
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우에 사용한다.
- 시간 복잡도는 O(N^3)이다.
- A -> B의 경로가 3일때, A -> 1 -> B가  2라는 것이 밝혀지면, A -> B의 경로를 2로 갱신한다.
- 'A에서 B로 가는 최소 비용'과 'A에서 K를 거쳐 B로 가는 비용'을 비교하여 더 작은 값으로 갱신하는 것이다.
```python
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
```

### 문제 - 미래 도시
- 문제 분석
  - 1번 회사 -> K번 회사 -> X번 회사
  - 최소 시간 계산
- 문제 해설
  - 전형적인 플로이드 워셜 알고리즘이다.