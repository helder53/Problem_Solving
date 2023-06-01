# My Solution
from collections import deque
def solution(k, dungeons):
    L,n,dp = len(dungeons),0,deque()
    dp.append([k,[]])
    while dp:
        p,v=dp.popleft()
        for i in range(L):
            [a,b]=dungeons[i]
            if i not in v and p>=a and p-b>=1: dp.append([p-b,v+[i]])
            else : n=max(n,len(v))
    return n
  
# Solutin By Others
import itertools
def others(k, dungeons):
    answer = -1
    visited = 0
    for dungeon_permutations in itertools.permutations(dungeons):
        have, count = k, 0
        for need, cost in dungeon_permutations:
            if have >= need and have >= cost:
                have -= cost
                count += 1
        visited = max(visited, count)
    answer = visited
    return answer