def solution(s):
    return s.isnumeric() and len(s) in [4, 6]

# false
print(solution("a234"))
# true
print(solution("1234"))