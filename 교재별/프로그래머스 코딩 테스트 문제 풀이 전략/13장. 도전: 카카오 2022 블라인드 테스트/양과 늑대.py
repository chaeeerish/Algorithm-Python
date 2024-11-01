answer = 0


def solution(info, edges):
    child = [[] for _ in range(len(info))]

    for p, c in edges:
        child[p].append(c)

    def dfs(now, sheep, wolf, able):
        global answer

        if wolf >= sheep:
            return
        if sheep > answer:
            answer = sheep

        able.extend(child[now])

        for a in able:
            if info[a]:
                dfs(a, sheep, wolf + 1, [i for i in able if i != a])
            else:
                dfs(a, sheep + 1, wolf, [i for i in able if i != a])

    dfs(0, 1, 0, child[0])

    return answer