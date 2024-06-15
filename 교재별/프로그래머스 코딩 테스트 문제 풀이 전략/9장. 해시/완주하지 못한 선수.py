def solution(participant, completion):
    dictionary = {}
    for p in participant:
        if p in dictionary:
            dictionary[p] += 1
        else:
            dictionary[p] = 1

    for c in completion:
        dictionary[c] -= 1

    for p in participant:
        if dictionary[p] != 0:
            return p

# leo
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
# vinko
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
# mislav
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))