def solution(s):
    stack = []
    for char in s:
        if len(stack) == 0 or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()

    return 1 if not stack else 0

# 1
print(solution("baabaa"))
# 0
print(solution("cdcd"))