def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def get_index(n):
    n = str(n)

    if n.isnumeric() and 1 <= int(n) <= 9:
        return int(n)
    elif n.isnumeric() and int(n) == 0:
        return 11
    elif n == '*':
        return 10
    elif n == '#':
        return 12

def solution(numbers, hand):
    answer = ''
    current_L = '*'
    current_R = '#'

    coordinate = [(-1, -1)]
    for r in range(4):
        for c in range(3):
            coordinate.append((r, c))

    # print("coordinate")
    # print(coordinate)

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            current_L = n
        elif n in [3, 6, 9]:
            answer += 'R'
            current_R = n
        else:
            left_index = get_index(current_L)
            right_index = get_index(current_R)
            n_index = get_index(n)

            left_distance = get_distance(coordinate[left_index][0], coordinate[left_index][1], coordinate[n_index][0], coordinate[n_index][1])
            right_distance = get_distance(coordinate[right_index][0], coordinate[right_index][1], coordinate[n_index][0], coordinate[n_index][1])

            if left_distance < right_distance:
                answer += 'L'
                current_L = n
            elif left_distance > right_distance:
                answer += 'R'
                current_R = n
            else: # left_distance == right_distance
                if hand == 'left':
                    answer += 'L'
                    current_L = n
                else:
                    answer += 'R'
                    current_R = n

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")) # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")) # "LLRLLRLLRL"
print(solution([], "right"))