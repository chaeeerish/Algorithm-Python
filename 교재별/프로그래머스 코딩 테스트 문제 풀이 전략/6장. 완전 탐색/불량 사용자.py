import copy
from itertools import product


def get_index_list(s):
    result = []
    for i in range(len(s)):
        if s[i] == '*':
            result.append(i)
    return result


def solution(user_id, banned_id):
    answer = 1
    for b in banned_id:
        index = get_index_list(b)
        cnt = 0

        for iter in product("abcdefghijklmnopqrstuvwxyng1234567890", repeat=b.count('*')):
            new_b = copy.deepcopy(b)
            temp = 0
            for i in index:
                new_b = new_b[:i] + iter[temp] + new_b[i+1:]
                temp += 1
            if new_b in user_id:
                print(new_b)
                cnt += 1

        # print(answer, "에", cnt, "를 곱합니다.")
        answer *= cnt

    return answer

# 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# 3
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))