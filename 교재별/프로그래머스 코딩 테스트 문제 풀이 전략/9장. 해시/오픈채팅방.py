def solution(record):
    answer = []

    닉네임 = dict()
    for r in record:
        data = r.split(" ")
        if data[0] == "Enter":
            닉네임[data[1]] = data[2]
        elif data[0] == "Leave":
            pass
        else:
            닉네임[data[1]] = data[2]

    for r in record:
        data = r.split(" ")
        if data[0] == "Enter":
            answer.append(닉네임[data[1]] + "님이 들어왔습니다.")
        elif data[0] == "Leave":
            answer.append(닉네임[data[1]] + "님이 나갔습니다.")
    return answer

# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))