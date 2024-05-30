def next(food_times, current):
    current = current + 1
    while True:
        if current >= len(food_times):
            current = 0
            continue

        if food_times[current] != 0:
            return current
        else:
            current = current + 1


def solution(food_times, k):
    answer = 0

    i = -1
    for time in range(k + 1):
        if all(x == 0 for x in food_times):
            return -1
        i = next(food_times, i)
        food_times[i] -= 1

    return i + 1