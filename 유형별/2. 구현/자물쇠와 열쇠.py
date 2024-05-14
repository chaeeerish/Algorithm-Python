import copy

# i: 행, j: 열
def rotate(key):
    result = []
    for j in range(len(key[0])): # 열 개수
        column = []
        for i in range(len(key)): # 행 개수
            column.insert(0, key[i][j])
        result.append(column)
    return result

def move_up(key, times):
    if times == 0:
        return key

    result = []
    for _ in range(times):
        result = []
        for i in range(1, len(key)):
            result.append(key[i])
        result.append([0] * len(key[0]))
        key = result
    return result

def move_down(key, times):
    if times == 0:
        return key

    result = []
    for _ in range(times):
        result = []
        result.append([0] * len(key[0]))
        for i in range(0, len(key) - 1):
            result.append(key[i])
        key = result
    return result

def move_right(key, times):
    if times == 0:
        return key

    result = []
    for _ in range(times):
        result = copy.deepcopy(key)
        for i in range(len(key)):
            result[i].insert(0, 0)
            result[i].pop()
        key = result
    return result

def move_left(key, times):
    if times == 0:
        return key

    result = []
    for _ in range(times):
        result = copy.deepcopy(key)
        for i in range(len(key)):
            del result[i][0]
            result[i].append(0)
        key = result
    return result

def compare(key, lock, count):
    for i in range(len(key)):
        for j in range(len(key[0])):
            if key[i][j] ^ lock[i][j] == 1:
                continue
            else:
                return False
    return True

def expand(key, lock):
    expand_key = copy.deepcopy(key)
    if (len(lock) - len(key)) > 0:
        for _ in range(len(lock) - len(key)):
            expand_key.append(([0] * len(key[0])))
    for i in range(len(lock)):
        expand_key[i].extend([0] * (len(lock[0]) - len(key[0])))
    return expand_key

def solution(key, lock):
    m = len(key)
    n = len(lock)
    move = n - 1

    count = 0
    for i in range(len(lock)):
        count += lock[i].count(0)

    expand_key = expand(key, lock)

    rotate_key = copy.deepcopy(expand_key)
    for _ in range(4):
        rotate_key = rotate(rotate_key)
        if compare(rotate_key, lock, count):
            return True

        for i in range(move + 1):
            up_key = move_up(rotate_key, i)
            if compare(up_key, lock, count):
                return True

            for j in range(move + 1):
                right_key = move_right(up_key, j)
                if compare(right_key, lock, count):
                    return True

            for j in range(move + 1):
                left_key = move_left(up_key, j)
                if compare(left_key, lock, count):
                    return True

        for i in range(move + 1):
            down_key = move_down(rotate_key, i)
            if compare(down_key, lock, count):
                return True

            for j in range(move + 1):
                right_key = move_right(down_key, j)
                if compare(right_key, lock, count):
                    return True

            for j in range(move + 1):
                left_key = move_left(down_key, j)
                if compare(left_key, lock, count):
                    return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])) # True
print(solution([[1, 0], [1, 1]], [[1, 1, 1, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]])) # True
print(solution([[1, 0], [1, 1]], [[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [1, 0, 1, 1]])) # False
print(solution([[0, 0], [0, 0]], [[1, 0, 0], [1, 0, 0], [1, 1, 1]])) # False

