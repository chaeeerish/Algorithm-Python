## 그래프 이론
### 다양한 그래프 알고리즘
- 그래프
  - 노드와 노드 사이에 연결된 간선의 정보를 가지고 있는 자료구조이다.
  - 알고리즘 문제를 접했을 때 '서로 다른 개체가 연결되어 있다'는 이야기를 들으면 가장 먼저 그래프 알고리즘을 떠올려야 한다.
  - '여러개의 도시가 연결되어 있다.'와 같은 내용이 등장하면 그래프 알고리즘을 의심해보자.
- 그래프 vs 트리

|속성|그래프|트리|
|------|---|---|
|방향성|방향 그래프 혹은 무방향 그래프|방향 그래프|
|순환성|순환 및 비순환|비순환|
|루트 노드 존재 여부|루트 노드가 없음|루트 노드가 존재|
|노드간 관계성|부모와 자식 관계 없음|부모와 자식 관계|
|모델의 종류|네트워크 모델|계층 모델|

- 그래프의 구현 방법
  - 인접 행렬
    - O(V^2)만큼의 메모리 공간이 필요하다.
    - 특정한 노드에서 다른 노드로 이어진 간선의 비용을 O(1)의 시간으로 즉시 알 수 있다.
  - 인접 리스트
    - O(E)만큼의 메모리 공간이 필요하다.
    - 특정한 노드에서 다른 노드로 이어진 간선의 비용을 O(V)의 시간이 소요된다.

- 서로소 집합
  - 서로소 집합 자료구조를 구현할 때는 트리 자료구조를 이용하여 집합을 표현한다.
  - A와 B의 합집합 알고리즘은 다음과 같다.
    - A와 B의 루트 노드 'A', 'B'를 각각 찾는다.
    - 'A'를 'B'의 부모 노드로 설정한다. == 'B'가 'A'를 가리키도록 한다.
    - (번호가 작은 노드가 부모가 되고, 번호가 큰 노드는 자식이 된다.)
    - 모든 연산을 처리할 때까지 1번 과정을 반복한다.
- 서로소 집합 알고리즘 코드
```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 경로 압축 적용
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end=" ")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print()

print('부모 테이블: ', end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")
```

- 서로소 집합을 이용한 **사이클 판별 알고리즘**
  - 간선을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합친다.
  - 모든 간선을 확인할 때까지 사이클이 생기지 않았다면 해당 그래프에는 사이클이 없다는 것을 알 수 있다.
```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 경로 압축 적용
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
```

- 신장 트리, Spanning Tree
  - 하나의 그래프가 있을 때 **모든 노드를 포함**하면서 **사이클이 존재하지 않는 부분 그래프**를 의미한다.
- 크루스칼 알고리즘
  - 다양한 문제 상황에서 최소한의 비용으로 신장 트리를 찾아야할 때가 있다.
  - 예를 들어, N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우를 생각해보자.
  - 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘을 '최소 신장 트리 알고리즘'이라고 한다.
  - 대표적인 최소 신장 트리 알고리즘에 크루스칼 알고리즘이 있다.
  - 크루스칼 알고리즘은 그리디 알고리즘으로 구련한다.
    - 간선을 비용에 따라 오름차순으로 정렬한다.
    - 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
  - 최종적으로 신장 트리에 포함되는 간선의 개수가 '노드의 개수 - 1'과 같다는 특징이 있다.
  - 시간 복잡도는 O(ElogE) 이다.
```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 경로 압축 적용
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent)
        result += cost
        
print(result)
```

- 위상 정렬, Topology Sort
  - 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘이다.
  - 방향성을 거스르지 않도록 순서대로 나열한다.
  - 대표적인 예시로는 '선수과목을 고려한 학습 순서 설정'이다.
  - '진입차수'란 특정한 노드로 들어오는 간선의 개수이다.
  - 위상 정렬 알고리즘은 다음과 같다.
    - 진입 차수가 0인 노드를 큐에 넣는다.
    - 큐가 빌 때까지 다음의 과정을 반복한다.
      - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
      - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
  - 큐에서 원소가 V번 추출되기 전에 큐가 비어버리면 사이클이 발생한 것이다.
  - 위상 정렬에서 시간 복잡도는 O(V+E)이다.
```python
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()
```

### 문제 - 팀 결성
- 문제 분석
  - 학생들은 0번부터 N번까지의 번호를 가지고 있다.
  - 처음에는 모든 학생들이 다른 팀이다.
  - '팀 합치기 연산': 두 팀을 합친다.
  - '같은 팀 여부 확인': 특정한 두 학생이 같은 팀에 속하는지 확인
  - M개의 연산을 수행했을 때, '같은 팀 여부 확인'에 대한 연산 결과를 출력하는 프로그램
- 문제 해설
  - 전형적인 서로소 집합 알고리즘 문제이다.
  - N과 M의 범위가 모두 최대 100,000이므로 경로 압축 방식의 서로소 집합 자료구조를 사용해야한다.

### 문제 - 도시 분할 계획
- 문제 분석
  - 마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.
  - 마을을 2개로 분리하려 한다.
  - 각 분리된 마을 안에 집들이 서로 연결되어 있어야 한다.
  - 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다.
  - 길의 유지비를 최소로 하는 프로그램을 만들어보자.
- 문제 해설
  - 크루스칼 알고리즘으로 최소 신장 트리를 찾은 다음에 최소 신장 트리를 구성하는 간선 중에서 비용이 가장 큰 간선을 제거한다.