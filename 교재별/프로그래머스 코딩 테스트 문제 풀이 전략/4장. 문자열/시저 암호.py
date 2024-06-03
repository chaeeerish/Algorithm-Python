def solution(s, n):
    answer = ''
    for al in s:
        if al == ' ':
            answer += ' '
        elif (al.islower() and ord(al) + n >= 123) or (al.isupper() and ord(al) + n >= 91):
            answer += chr(ord(al) + n - 26)
        else:
            answer += chr(ord(al) + n)
    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))