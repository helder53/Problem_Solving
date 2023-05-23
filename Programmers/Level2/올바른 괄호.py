# My Solution
from collections import deque
def solution(s):
    t = deque([])
    
    for i in s:
        if len(t)==0:
            t.append(i)
        else:
            if t[-1]=='(' and i == ')':
                t.pop()
            else:
                t.append(i)
    
    return True if len(t)==0 else False

# Solution By Others
def others(s):
    answer = 0
    for i in s:
        if i == '(':
            answer += 1
        elif i == ')':
            answer -= 1
        if answer < 0: 
            return False
    return answer == 0