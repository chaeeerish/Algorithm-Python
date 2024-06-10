def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isnumeric():
        return True
    return False

# false
print(solution("a234"))
# true
print(solution("1234"))