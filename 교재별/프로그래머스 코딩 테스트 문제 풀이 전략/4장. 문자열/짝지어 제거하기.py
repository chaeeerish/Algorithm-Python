def solution(s):
    i = 0
    while True:
        if i >= len(s) - 1:
            break

        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            if i == 0:
                i = 0
            else:
                i = i - 1
        else:
            i += 1

    if s == '':
        return 1
    else:
        return 0

# 1
print(solution("baabaa"))
# 0
print(solution("cdcd"))