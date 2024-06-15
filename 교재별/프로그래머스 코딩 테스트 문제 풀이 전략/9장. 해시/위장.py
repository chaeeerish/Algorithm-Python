def solution(clothes):
    dictionary = dict()
    for c in clothes:
        name, type = c[0], c[1]
        if type in dictionary:
            dictionary[type].append(name)
        else:
            dictionary[type] = [name]

    print(dictionary)

    if len(dictionary.keys()) == 1:
        return len(dictionary[c[1]])

    answer = 1
    for k in dictionary.keys():
        answer *= (len(dictionary[k]) + 1)

    return answer - 1

# 5
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
# 3
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))