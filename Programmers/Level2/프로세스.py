# My Solution
from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([x for x in priorities])
    t = deque([0 for _ in range(len(priorities))])
    t[location] = 1


    while True:
        if t.count(1) == 0:
            break

        if q[0] == max(q):
            q.popleft()
            t.popleft()
            answer += 1

        elif q[0] < max(q):
            q.append(q.popleft())
            t.append(t.popleft())
    
    return answer

# Solution By Others
def others(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer