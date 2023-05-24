# My Solution
def solution(s, skip, index):
    result = ""

    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in skip:
        alp.pop(alp.index(i))

    for word in s:
        idx = alp.index(word)+index
        if idx >= len(alp):
            idx = idx % len(alp)
        result += alp[idx]
        
    return result
  
# Solution By Others
from string import ascii_lowercase

def others(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result