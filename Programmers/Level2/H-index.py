# My Solution
def solution(citations):
    c = sorted(citations)

    for idx, j in enumerate(c):
        if j >= len(c) - idx:
            return len(c) - idx
    return 0
  
# Solution By Others
def others(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer