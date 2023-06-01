# My Solution
from collections import deque

def solution(progresses, speeds):
    answer = []
    p = deque([x for x in progresses])
    s = deque([x for x in speeds])

    while True:
        if sum(answer) == len(progresses):
            break
        
        for i in range(len(p)):
            p[i] += s[i]

        count = 0
        while p:
            if p[0] >= 100:
                count += 1
                p.popleft()
                s.popleft()
            else:
                break
        
        if count != 0:
            answer.append(count)
    
    return answer

# Solution By Others
from collections import deque

def others(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        a=0
        while 1:
            if progresses[0] >= 100:
                a+=1
                progresses.popleft()
                speeds.popleft()
                if len(progresses) == 0 and a >0:
                    answer.append(a)
                    break
            else:
                if a>0:
                    answer.append(a)
                for i in range(len(progresses)):
                    progresses[i]+=speeds[i]
                break
    return answer