# My Solution
def solution(book_time):
    answer = 0
    t = []

    for start,end in book_time:
        t.append([int(start[:2])*60+int(start[3:]),1])
        t.append([int(end[:2])*60+int(end[3:])+10,-1])
    t.sort()

    room = 0
    for i in t:
        room += i[1]
        answer=max(answer, room)
    return answer
  
# Solution By Others
from heapq import heappop, heappush
def others(book_time):
    answer = 1
    book_time_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time_ref.sort()

    heap = []
    for s, e in book_time_ref:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e+10)

    return answer