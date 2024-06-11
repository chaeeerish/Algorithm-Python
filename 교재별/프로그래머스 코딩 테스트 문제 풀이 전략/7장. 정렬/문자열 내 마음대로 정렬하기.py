def solution(strings, n):
    strings.sort(key=lambda x: x[n])

    answer = []

    sort_list = []
    sort_list.append(strings[0])
    cnt = 1
    while cnt <= len(strings) - 1:
        if strings[cnt - 1][n] == strings[cnt][n]:
            sort_list.append(strings[cnt])
        else:
            sort_list.sort()
            answer.extend(sort_list)
            sort_list.clear()
            sort_list.append(strings[cnt])
        cnt += 1

    sort_list.sort()
    answer.extend(sort_list)
    return answer

# ["car", "bed", "sun"]
print(solution(["sun", "bed", "car"], 1))
# ["abcd", "abce", "cdx"]
print(solution(["abce", "abcd", "cdx"], 2))