import itertools


def solution(word): # 0: 'A', 1: 'E', 2: 'I', 3: 'O', 4: 'U'
    answer = 0
    alphabet = list("AEIOU")
    array = []
    for i in range(1, 6):
        for iter_list in list(itertools.product(alphabet, repeat=i)):
            array.append("".join(iter_list))
    array.sort()

    return array.index(word) + 1

# 6
print(solution("AAAAE"))
# 10
print(solution("AAAE"))
# 1563
print(solution("I"))
# 1189
print(solution("EIO"))