"""
구조물은 교차점 기준으로 오른쪽, 기둥은 위쪽으로 설치 또는 삭제된다.
"""
"""
build_frame
[1,0,0,1]: (1, 0)에 기둥을 설치한다.
[1,1,1,1]: (1, 1)에 보를 설치한다.
[2,1,0,1]: (2, 1)에 기둥을 설치한다.
[2,2,1,1]: (2, 2)에 보를 설치한다.
[5,0,0,1]: (5, 0)에 기둥을 설치한다.
[5,1,0,1]: (5, 1)에 기둥을 설치한다.
[4,2,1,1]: (4, 2)에 보를 설치한다.
[3,2,1,1]: (3, 2)에 보를 설치한다.
"""
"""
최종 구조물
[1,0,0]: (1, 0)에 기둥이 설치되어 있다.
[1,1,1]: (1, 1)에 보가 설치되어 있다.
[2,1,0]: (2, 1)에 기둥이 설치되어 있다.
[2,2,1]: (2, 2)에 보가 설치되어 있다.
[3,2,1]: (3, 2)에 보가 설치되어 있다.
[4,2,1]: (4, 2)에 보가 설치되어 있다.
[5,0,0]: (5, 0)에 기둥이 설치되어 있다.
[5,1,0]: (5, 1)에 기둥이 설치되어 있다.
"""
import copy

def check_existence(answer, x, y, type):
    if (x, y) in answer.keys():
        if type in answer[(x, y)]:
            return True
        else:
            return False
    else:
        return False

def check_rule(answer):
    for key in answer:
        if 0 in answer[key]: # 기둥
            if key[0] == 0:
                continue
            if check_existence(answer, key[0], key[1], 1):
                continue
            if check_existence(answer, key[0], key[1] - 1, 1):
                continue
            if check_existence(answer, key[0] - 1, key[1], 0):
                continue
            return False
        if 1 in answer[key]: # 보
            if check_existence(answer, key[0] - 1, key[1], 0):
                continue
            if check_existence(answer, key[0] - 1, key[1] + 1, 0):
                continue
            if check_existence(answer, key[0], key[1] - 1, 1) and check_existence(answer, key[0], key[1] + 1, 1):
                continue
            return False
    return True


def build(answer, seq):
    new_answer = copy.deepcopy(answer)
    if (seq[0], seq[1]) in new_answer.keys():
        if seq[-1] == 1: # 설치
            new_answer[(seq[0], seq[1])].add(seq[2])
        else:
            if seq[2] in new_answer[(seq[0], seq[1])]:
                new_answer[(seq[0], seq[1])].remove(seq[2])
    else:
        if seq[-1] == 1:  # 설치
            new_answer[(seq[0], seq[1])] = {seq[2]}

    if check_rule(new_answer):
        return new_answer
    else:
        return answer

def solution(n, build_frame):
    for i in range(len(build_frame)):
        build_frame[i][0], build_frame[i][1] = build_frame[i][1], build_frame[i][0]

    answer = dict()
    for seq in build_frame:
        answer = build(answer, seq)

    result = []
    for k in answer.keys():
        v = answer[k]
        if len(v) == 0:
            continue
        elif len(v) == 1:
            result.append([k[1], k[0], v.pop()])
        elif len(v) == 2:
            result.append([k[1], k[0], v.pop()])
            result.append([k[1], k[0], v.pop()])
    result.sort(key=lambda x: (x[0], x[1], x[2]))

    return result

# print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
# print(solution(5, [[1, 0, 0, 1], [2, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 0, 0, 0]])) # [[0, 1, 1], [1, 0, 0], [1, 1, 1], [2, 0, 0]]
