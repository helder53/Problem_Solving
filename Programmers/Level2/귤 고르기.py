# My Solution
import operator

def solution(k, tangerine):
    result = 0
    h = {x:0 for x in tangerine}
    for i in tangerine:
        h[i] += 1

    t = sorted(h.items(), key=operator.itemgetter(1), reverse=True)

    for i, j in t:
        if k > 0:
            k -= j
            result += 1
        else:
            continue
    return result
  
# Solution By Others
import collections

def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer