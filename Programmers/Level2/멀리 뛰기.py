# My Solution
def solution(n):
    s = [1 for i in range(n+1)]
    for i in range(2, n+1):
        s[i] = s[i-1] + s[i-2]

    return s[n] % 1234567

# Solution By Others
def others(n):
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return b % 1234567