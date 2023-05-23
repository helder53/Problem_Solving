# My Solution
def solution(s):
    t = []
    for i in s.split(" "):
        t.append(i.capitalize())
    return ' '.join(t)
  
# Solution By Others
def others(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])