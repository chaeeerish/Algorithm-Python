def solution(gems):
    type = set(gems)

    if len(type) == 1:
        return [1, 1]

    start = 0
    end = 1
    cand = dict()

    for t in type:
        cand[t] = 0

    cand[gems[start]] = 1
    cand[gems[end]] = 1

    min_length = 1000002
    min_start = 0
    min_end = 0

    validate_count = 2

    while start <= len(gems) - 1 and end <= len(gems) - 1:
        # print("start, end =", start, end)
        # print(cand)
        if validate_count == len(type):
            # print("위는 TRUE")
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_start = start
                min_end = end
            cand[gems[start]] -= 1
            if cand[gems[start]] == 0:
                validate_count -= 1
            start += 1
            continue

        if end == len(gems) - 1:
            cand[gems[start]] -= 1
            if cand[gems[start]] == 0:
                validate_count -= 1
            start += 1
        else:
            end += 1
            if cand[gems[end]] == 0:
                validate_count += 1
            if end <= len(gems) - 1:
                cand[gems[end]] += 1

    return [min_start + 1, min_end + 1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # [3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) # [1, 3]
print(solution(["XYZ", "XYZ", "XYZ"])) # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) # [1, 5]