# My Solution( fail[Runtime error] )
'''
def solution(r1, r2):
    line = 0
    answer = 0
    for x in range(r2+1):
        for y in range(r2+1):
            t = x*x + y*y
            if (r1**2) <= t and (r2**2) >= t:
                if x == 0 or y == 0: 
                    line += 2
                else:
                    answer += 4
    return answer + line
'''

# Solution By Others
from math import floor, ceil, sqrt

def others(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        m = floor(sqrt(r2**2-x**2))
        n = 0 if x>r1 else ceil(sqrt(r1**2-x**2))
        answer += m-n+1
    return answer * 4