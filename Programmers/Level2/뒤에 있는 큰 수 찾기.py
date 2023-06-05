# My Solution
def solution(numbers):
    answer = [-1]*len(numbers)
    for i in range(len(numbers)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if numbers[j] >= numbers[i]:    break
            answer[j] = numbers[i]

    return answer

# Solution By Others
def others(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
        stack.append(i)

    return result