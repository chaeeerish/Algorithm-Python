# https://www.notion.so/hyehwa-cs/de40f94bb781469990857b5ba1e77887
import itertools


def solution(orders, course):
    answer = set()

    candidates = dict()
    for order in orders:
        for c in course:
            for iter in itertools.combinations(sorted(order), c):
                key = ''.join(iter)
                candidates[key] = candidates.get(key, 0) + 1

    for c in course:
        max_value = 0
        for key in candidates.keys():
            if len(key) == c and candidates[key] >= 2:
                max_value = max(max_value, candidates[key])

        for key in candidates.keys():
            if len(key) == c and candidates[key] == max_value:
                answer.add(key)

    new_answer = list(answer)
    new_answer.sort()
    return new_answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))