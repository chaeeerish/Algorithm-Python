from collections import deque

t = int(input())

answer = []
for _ in range(t):
    n = int(input())
    last_year = list(map(int, input().split())) # 5 4 3 2 1

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(len(last_year)):
        for j in range(i + 1, len(last_year)):
            graph[last_year[j]].append(last_year[i])

    count = 0
    for i in range(len(last_year) - 1, -1, -1):
        indegree[last_year[i]] = count
        count += 1

    m = int(input())
    modified = []
    for _ in range(m):
        modified.append(tuple(map(int, input().split())))

    flag = True
    for i in range(m): # 2 4 : 2가 4보다 먼저
        if modified[i][1] in graph[modified[i][0]]:
            graph[modified[i][0]].remove(modified[i][1])
            graph[modified[i][1]].append(modified[i][0])
            indegree[modified[i][1]] -= 1
            indegree[modified[i][0]] += 1
        else:
            graph[modified[i][1]].remove(modified[i][0])
            graph[modified[i][0]].append(modified[i][1])
            indegree[modified[i][0]] -= 1
            indegree[modified[i][1]] += 1

    # print(graph) # [[], [5, 4, 3, 2], [5, 4, 3], [5, 4], [5], []]
    # print(indegree) # [0, 0, 1, 2, 3, 4]
    # print(modified) # [(2, 4), (3, 4)]
    # print()

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) != n:
        answer.append("IMPOSSIBLE")
    else:
        result.reverse()
        answer.append(result)

for a in answer:
    if a != "IMPOSSIBLE" and a != "?":
        for item in a:
            print(item, end=" ")
        print()
    else:
        print(a)


"""
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
"""

"""
# 3 1 2
1
3
1 3 2
1
1 3
"""