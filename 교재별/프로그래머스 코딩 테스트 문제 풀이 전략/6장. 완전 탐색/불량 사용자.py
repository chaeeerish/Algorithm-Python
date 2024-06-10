import re
import itertools


def solution(user_id, banned_id):
    available = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        b = banned_id[i]
        new_b = b.replace('*', '[a-z0-9]')
        p = re.compile(new_b)

        for u in user_id:
            if len(b) == len(u) and p.match(u):
                available[i].append(u)

    result = []
    for iter in itertools.product(*available):
        if len(banned_id) == len(set(iter)) and set(iter) not in result:
            result.append(set(iter))

    return len(result)

# 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# 3
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))