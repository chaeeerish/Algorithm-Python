def find_parent(parent, x):
    if (parent[x] != x):
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    answer = 0

    parent = [i for i in range(len(computers))]

    for i in range(len(computers)):
        for j in range(len(computers)):
            if computers[j][i] == 1:
                union_parent(parent, i, j)

    for i in range(len(parent)):
        find_parent(parent, i)

    return len(set(parent))