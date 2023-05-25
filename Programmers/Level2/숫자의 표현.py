# My Solution
def solution(n):
    answer = 0
    for i in range(1, n//2+2):
        s = 0
        s += i
        for j in range(i+1, n//2+2):
            s += j
            if s == n:
                answer += 1
                break
            elif s > n:
                break
    return answer+1
  
  
# Solution By Others
def others(n):
    answer = 0
    cnt = 0
    for i in range(1,n+1) :
        if i % 2 != 0 and n % i == 0 :
            cnt += 1
    return cnt