answer = 0

def dfs(numbers, index, target):
    global answer

    if index == len(numbers):
        if target == 0:
            return True
        else:
            return False
    else:
        if dfs(numbers, index+1, target + numbers[index]):
            answer += 1
        if dfs(numbers, index+1, target - numbers[index]):
            answer += 1

def solution(numbers, target):
    global answer

    dfs(numbers, 0, target)
    return answer

print(solution([1, 1, 1, 1, 1], 3)) # 5
print(solution([4, 1, 2, 1], 4)) # 2