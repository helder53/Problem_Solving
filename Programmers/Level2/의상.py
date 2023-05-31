# My Solution
import itertools
import math

def solution(clothes):
    s = {}
    
    for i, j in clothes:
        if j not in s:
            s[j] = [i]
        else: s[j] += [i]

    answer = 1
    for i in s:
        answer *= len(s[i]) + 1
    
    return answer - 1

# Solution By Others
from collections import Counter
from functools import reduce

def others(clothes):    
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer