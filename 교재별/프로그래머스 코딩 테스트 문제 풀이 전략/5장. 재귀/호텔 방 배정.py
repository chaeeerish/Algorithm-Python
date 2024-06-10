def solution(k, room_number):
    answer = []
    is_allocated = {}
    for i in range(1, k + 1):
        is_allocated[i] = False

    for wish_number in room_number:
        if is_allocated[wish_number] == False:
            is_allocated[wish_number] = True
            answer.append(wish_number)
        else:
            while True:
                wish_number += 1
                if is_allocated[wish_number] == False:
                    is_allocated[wish_number] = True
                    answer.append(wish_number)
                    break

    return answer

# [1, 3, 4, 2, 5, 6]
print(solution(10, [1, 3, 4, 1, 3, 1]))