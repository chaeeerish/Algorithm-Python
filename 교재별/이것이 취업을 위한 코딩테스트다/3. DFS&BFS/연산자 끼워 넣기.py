import math, copy

n = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))

maxResult = -1
minResult = math.inf

def operate(n1, n2, operator):
    if operator == 0:
        return add(n1, n2)
    elif operator == 1:
        return subtract(n1, n2)
    elif operator == 2:
        return multiply(n1, n2)
    elif operator == 3:
        return divide(n1, n2)
    return -1

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n1 * n2 < 0:
        return - (abs(n1) // abs(n2))
    return n1 // n2

def updateMaxResult(result):
    global maxResult
    maxResult = max(maxResult, result)

def updateMinResult(result):
    global minResult
    minResult = min(minResult, result)

def calculate(number, operator):
    if len(number) == 1:
        return number[0]

    for i in range(4):
        operator_copy = copy.deepcopy(operator)
        if operator_copy[i] >= 1:
            temp = operate(number[0], number[1], i)
            operator_copy[i] -= 1
            result = calculate([temp] + number[2:], operator_copy)
            if result != None:
                updateMaxResult(result)
                updateMinResult(result)

calculate(number, operator)
print(maxResult)
print(minResult)

"""
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1
"""