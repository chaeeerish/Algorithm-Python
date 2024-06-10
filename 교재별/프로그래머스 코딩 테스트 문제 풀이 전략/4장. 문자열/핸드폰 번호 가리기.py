def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]

# "*******4444"
print(solution("01033334444"))
# "*****8888"
print(solution("027778888"))