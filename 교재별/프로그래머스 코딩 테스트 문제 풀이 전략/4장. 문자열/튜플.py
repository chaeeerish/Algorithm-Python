def solution(s):
    s = s[1:-2] # {2},{2,1},{2,1,3},{2,1,3,4}
    array = [set() for _ in range(len(s.split(",{")))]

    index = -1
    tmp = ''
    for i in range(len(s)):
        if s[i] == '{':
            index += 1
        elif s[i] == '}' and tmp != '':
            array[index].add(int(tmp))
            tmp = ''
        elif s[i].isdecimal():
            tmp += s[i]
        elif s[i] == ',' and s[i - 1] != '}':
            array[index].add(int(tmp))
            tmp = ''
    if tmp != '':
        array[index].add(int(tmp))

    array.sort(key=lambda x: len(x))

    answer = []
    answer.append((array[0] - set()).pop())
    for j in range(1, len(array)):
        answer.append((array[j] - array[j - 1]).pop())
    return answer

# [2, 1, 3, 4]
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# [111, 20]
print(solution("{{20,111},{111}}"))
# [123]
print(solution("{{123}}"))
# [3, 2, 4, 1]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))