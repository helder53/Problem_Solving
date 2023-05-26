# My Solution
def solution(n):
    s = [0 for i in range(n+1)]
    s[1] = 1
    if n < 2:
        return s[n]
    else:
        for i in range(2, n+1):
            s[i] = s[i-1] + s[i-2]
        return s[n] % 1234567
      
# Solution By Others
def others(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a % 1234567