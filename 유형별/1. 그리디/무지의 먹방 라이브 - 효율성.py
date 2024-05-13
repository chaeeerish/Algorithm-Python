# 다음의 해설 영상을 참고하였습니다.
# https://www.youtube.com/watch?v=zpz8SMzwiHM

from operator import itemgetter

def solution(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i + 1))
    foods.sort()

    pretime = 0
    for i, food in enumerate(foods):
        diff = food[0] - pretime
        if diff != 0:
            spend = diff * n
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key=itemgetter(1))
                return sublist[k][1]
        n -= 1

    return -1