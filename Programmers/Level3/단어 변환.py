# My Solution
from collections import deque

def DFS(t, begin, target):
  result = 51
  vis = []
  Q = deque()
  Q.append(begin)
  
  while Q:
    node = Q.pop()
    if node not in vis:
      vis.append(node)
      Q.extend(t[node])
    
    if vis[0]==begin and vis[-1]==target:
      result = min(result, len(vis)-1)

  return 0 if result == 51 else result

def solution(begin, target, words):
  t = {x:[] for x in words}
  t[begin] = []
  for s in t:
    for word in words:
      cnt = 0
      for i in range(len(s)):
        if s[i] != word[i]:
          cnt += 1
        if cnt > 2:
          continue
      if cnt == 1:
        t[s].append(word)
      else:
        continue
  
  return DFS(t, begin, target)

# Solution By Others
def others(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = []
        for word_1 in Q:
            if word_1 == target:
                    return answer
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                if sum([x!=y for x, y in zip(word_1, word_2)]) == 1:
                    temp_Q.append(words.pop(i))

        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1