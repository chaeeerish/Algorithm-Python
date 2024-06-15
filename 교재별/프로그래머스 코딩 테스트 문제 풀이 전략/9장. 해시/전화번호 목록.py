def solution(phone_book):
    dictionary = dict()
    for p in phone_book:
        for i in range(1, len(p)):
            dictionary[p[0:i]] = True

    for p in phone_book:
        if p in dictionary:
            return False
    return True

# False
print(solution(["119", "97674223", "1195524421"]))
# True
print(solution(["123", "456", "789"]))
# False
print(solution(["12", "123", "1235", "567", "88"]))