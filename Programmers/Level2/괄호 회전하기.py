# My Solution
from collections import deque;

def chk(t):
  test = deque([])
  for i in t:    
    if len(test)>=1:
      if i == "}" and test[-1] == "{":
        test.pop()
      elif i == "]" and test[-1] == "[":
        test.pop()
      elif i == ")" and test[-1] == "(":
        test.pop()
      else:
        test.append(i)
    else:
      test.append(i)

  if test == deque([]):
    return True
  else:
    return False

def solution(s):
  t = deque([_ for _ in s])

  ans = 0
  for i in range(len(t)):
    t.append(t.popleft())
    if chk(t):
      ans += 1
  return ans

# Solution By Others
from collections import deque

def check(s):
    while True:
        if "()" in s: s=s.replace("()","")
        elif "{}" in s: s=s.replace("{}","")
        elif "[]" in s: s=s.replace("[]","")
        else: return False if s else True       

def solution(s):
    ans = 0
    que = deque(s)

    for i in range(len(s)):
        if check(''.join(que)): ans+=1
        que.rotate(-1)
    return ans