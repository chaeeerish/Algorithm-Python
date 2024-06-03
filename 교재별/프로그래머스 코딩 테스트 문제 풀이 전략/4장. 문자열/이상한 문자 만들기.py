def solution(s):
    answer = ''

    even = True
    for char in s:
        if char == ' ':
            answer += ' '
            even = True
        else:
            answer += char.upper() if even else char.lower()
            even = not even

    return answer

# "TrY HeLlO WoRlD"
print(solution("try hello world"))