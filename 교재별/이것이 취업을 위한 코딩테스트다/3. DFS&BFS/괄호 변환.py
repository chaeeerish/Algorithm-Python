def 올바른_괄호_문자열(p): # True: 올바른 괄호 문자열 False: 균형잡힌 괄호 문자열
    stack = []
    for s in p:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
        else:
            continue
    if len(stack) != 0:
        return False
    return True

def 괄호_뒤집기(p):
    array = list(map(str, p))
    for i in range(len(array)):
        if array[i] == ')':
            array[i] = '('
        elif array[i] == '(':
            array[i] = ')'
    return "".join(array)

def seperate(p):
    if len(p) == 0:
        return ""
    if 올바른_괄호_문자열(p):
        return p

    u = ""
    v = ""
    for pin in range(1, len(p), 2):
        u = p[0: pin + 1]
        print("u =", u)
        v = p[pin + 1: len(p)]
        if u.count('(') != 0 and u.count('(') == u.count(')'):
            break

    # print("u =", u)
    if 올바른_괄호_문자열(u):
        return u + seperate(v)
    else:
        return '' + '(' + seperate(v) + ')' + 괄호_뒤집기(u[1:-1])

def solution(p):
    answer = seperate(p)
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))