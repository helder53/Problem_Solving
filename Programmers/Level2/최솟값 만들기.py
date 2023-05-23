# My Solution
def solution(A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)

    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

# Solution By Others
def others(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])