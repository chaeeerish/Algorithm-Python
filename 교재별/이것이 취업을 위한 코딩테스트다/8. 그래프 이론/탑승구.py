import math


def get_g(p):
    global graph_p
    cand_list = graph_p[p]

    min_count = math.inf
    min_index = -1
    for cand in cand_list:
        count = 0
        for p_list in graph_p:
            if cand in p_list:
                count += 1
        if count < min_count:
            min_count = count
            min_index = cand
    return min_index

G = int(input())
P = int(input())

visited_g = [False] * (G + 1)

graph_p = [[] for _ in range(P + 1)]

for p in range(1, P + 1):
    gi = int(input())
    for g in range(gi, 0, -1):
        graph_p[p].append(g)

for p in range(1, P + 1):
    if len(graph_p[p]) == 0:
        break

    g = get_g(p)
    visited_g[g] = True
    for p_list in graph_p:
        if g in p_list:
            p_list.remove(g)

print(visited_g.count(True))

"""
# 2
4
3
4
1
1

# 3
4
6
2
2
3
3
4
4
"""
