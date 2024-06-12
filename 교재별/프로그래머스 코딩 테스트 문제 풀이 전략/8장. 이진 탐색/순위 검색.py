def bisect_left(score, x):
    left = 0
    right = len(score) - 1
    while left <= right:
        mid = (left + right) // 2
        if score[mid] >= x:
            right = mid - 1
        else:  # score[mid] < x
            left = mid + 1
    return left


def solution(info, query):
    dictionary = dict()
    for language in ["cpp", "java", "python", "-"]:
        for part in ["backend", "frontend", "-"]:
            for career in ["junior", "senior", "-"]:
                for soulfood in ["chicken", "pizza", "-"]:
                    dictionary[language + part + career + soulfood] = []

    for i in info:
        data = i.split(" ")
        for language in [data[0], "-"]:
            for part in [data[1], "-"]:
                for career in [data[2], "-"]:
                    for soulfood in [data[3], "-"]:
                        dictionary[language + part + career + soulfood].append(int(data[4]))

    for language in ["cpp", "java", "python", "-"]:
        for part in ["backend", "frontend", "-"]:
            for career in ["junior", "senior", "-"]:
                for soulfood in ["chicken", "pizza", "-"]:
                    dictionary[language + part + career + soulfood].sort()

    answer = []
    for q in query:
        data = q.split(" ")
        array = dictionary[data[0] + data[2] + data[4] + data[6]]
        left_index = bisect_left(array, int(data[7]))
        answer.append(len(array) - left_index)

    return answer

# [1, 1, 1, 1, 2, 4]
print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))