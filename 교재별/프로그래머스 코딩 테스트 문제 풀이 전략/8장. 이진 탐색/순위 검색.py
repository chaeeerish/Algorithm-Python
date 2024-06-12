def bisect_left(score, x):
    left = 0
    right = len(score) - 1
    while left <= right:
        mid = (left + right) // 2
        if score[mid][0] >= x:
            right = mid - 1
        else: # score[mid][0] < x
            left = mid + 1
    return left

def solution(info, query):
    language = {"cpp": set(), "java": set(), "python": set(), "-": set(range(len(info)))}
    part = {"backend": set(), "frontend": set(), "-": set(range(len(info)))}
    career = {"junior": set(), "senior": set(), "-": set(range(len(info)))}
    soulfood = {"chicken": set(), "pizza": set(), "-": set(range(len(info)))}
    score = []

    for i in range(len(info)):
        data = info[i].split(" ")
        language[data[0]].add(i)
        part[data[1]].add(i)
        career[data[2]].add(i)
        soulfood[data[3]].add(i)
        score.append((int(data[4]), i))
    score.sort()

    answer = []
    for q in query: # cpp and - and senior and pizza 250
        data = q.split(" ")
        if data[7] != "-":
            left_index = bisect_left(score, int(data[7]))
            applicant = language[data[0]] & part[data[2]] & career[data[4]] & soulfood[data[6]] & set([a[1] for a in score[left_index:]])
        else:
            applicant = language[data[0]] & part[data[2]] & career[data[4]] & soulfood[data[6]]
        answer.append(len(applicant))
    return answer

# [1, 1, 1, 1, 2, 4]
print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))