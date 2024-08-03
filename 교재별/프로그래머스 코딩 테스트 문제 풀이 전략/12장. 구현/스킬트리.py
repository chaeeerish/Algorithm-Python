from collections import deque


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        queue = deque(skill_tree)

        current_skill = 0
        flag = True
        while queue:
            elem = queue.popleft()
            if elem in skill:
                if elem == skill[current_skill]:
                    current_skill = current_skill + 1
                else:
                    flag = False
                    break

        if flag:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2