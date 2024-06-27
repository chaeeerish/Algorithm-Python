def solution(S):
    stack = []
    for i in range(len(S)):
        if S[i] == '(':
            stack.append(S[i])
        else: # S[i] == ')'
            if len(stack) == 0:
                return 0
            stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0

print(solution('(()(())())'))
print(solution('())'))