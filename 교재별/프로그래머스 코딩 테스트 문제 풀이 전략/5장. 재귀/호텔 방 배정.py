import sys
sys.setrecursionlimit(100000)


def find(number, room):
    if number not in room:
        room[number] = number + 1
        return number

    empty = find(room[number], room)
    room[number] = empty + 1
    return empty


def solution(k, room_number):
    answer = []
    dic = {}

    for i in room_number:
        num = find(i, dic)
        answer.append(num)

    return answer
