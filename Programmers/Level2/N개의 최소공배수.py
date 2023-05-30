# My Solution
def f(a, b):                # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def solution(arr):
    while len(arr) >= 2:
        a = arr.pop()
        b = arr.pop()
        c = a * b // f(a,b)

        arr.append(c)
    return arr[0]
  
# Solution By Others
from fractions import gcd

def others(num):
    answer = num[0]
    for i in num:
        answer = i * answer / gcd(i, answer)
    return answer
  