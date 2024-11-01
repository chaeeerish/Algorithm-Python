def time_diff(start, end):
    # 05:34, 07:59 => 145분

    hour1 = int(start.split(":")[0])
    minute1 = int(start.split(":")[1])

    hour2 = int(end.split(":")[0])
    minute2 = int(end.split(":")[1])

    return (hour2 * 60 + minute2) - (hour1 * 60 + minute1)


def 크거나_같은_최소_정수(number):
    if int(number) == number:
        return number
    else:
        return int(number) + 1


def solution(fees, records):
    answer = []

    기본_시간 = fees[0]
    기본_요금 = fees[1]
    단위_시간 = fees[2]
    단위_요금 = fees[3]

    들어온_차량_시각 = dict()
    누적_차량_시간 = dict()
    for r in records:
        시각 = r.split(" ")[0]
        차량번호 = r.split(" ")[1]
        IN_OUT = r.split(" ")[2]

        if IN_OUT == "IN":
            들어온_차량_시각[차량번호] = 시각
        else:  # IN_OUT == "OUT":
            머문_시간 = time_diff(들어온_차량_시각[차량번호], 시각)
            if 차량번호 in 누적_차량_시간.keys():
                누적_차량_시간[차량번호] += 머문_시간
            else:
                누적_차량_시간[차량번호] = 머문_시간
            del 들어온_차량_시각[차량번호]

    for 차량번호 in 들어온_차량_시각.keys():
        머문_시간 = time_diff(들어온_차량_시각[차량번호], "23:59")
        if 차량번호 in 누적_차량_시간.keys():
            누적_차량_시간[차량번호] += 머문_시간
        else:
            누적_차량_시간[차량번호] = 머문_시간

    for 차량번호 in sorted(누적_차량_시간.keys()):
        if 누적_차량_시간[차량번호] < 기본_시간:
            answer.append(기본_요금)
        else:
            answer.append(기본_요금 + 크거나_같은_최소_정수((누적_차량_시간[차량번호] - 기본_시간) / 단위_시간) * 단위_요금)

    return answer