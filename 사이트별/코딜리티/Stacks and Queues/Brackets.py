def solution(S):
    if len(S) == 0:
        return 1

    stack = []
    i = 0
    while i <= len(S) - 1:
        if S[i] == '{' or S[i] == '[' or S[i] == '(':
            stack.append(S[i])
        else: # S[i] == '}' or S[i] == ']' or S[i] == ')':
            if len(stack) == 0:
                break
            elem = stack.pop()

            if S[i] == '}' and elem != '{':
                return 0
            elif S[i] == ']' and elem != '[':
                return 0
            elif S[i] == ')' and elem != '(':
                return 0
        i += 1

    if i == len(S) and len(stack) == 0:
        return 1
    return 0

print(solution('{[()()]}'))
print(solution('([)()]'))
print(solution(''))
print(solution('((]]()[]))'))