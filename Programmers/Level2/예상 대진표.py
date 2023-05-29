# My Solution
import math

def solution(n, a, b):
    x, y = min(a, b), max(a, b)

    ans = 0
    while (x!=y):
        x = math.ceil(x/2)
        y = math.ceil(y/2)
        ans += 1
    return ans
  
# Solution By Others
def others(n,a,b):
    return ((a-1)^(b-1)).bit_length()