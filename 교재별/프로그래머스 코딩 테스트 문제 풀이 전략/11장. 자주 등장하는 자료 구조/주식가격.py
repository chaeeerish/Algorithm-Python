def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = [0]  # 0번째 인덱스

    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer