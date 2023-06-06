# My Solution
def compare(list_mrl):
  dia = 0
  iron = 0
  stone = 0

  for i in list_mrl:
    dia += 1
    if i == 'diamond':
      iron += 5
      stone += 25
    elif i == 'iron':
      iron += 1
      stone += 5
    else:
      iron += 1
      stone += 1
    
  return [dia, iron, stone]

def solution(picks, minerals):
  minerals = minerals[:sum(picks)*5]
  answer = 0
  
  t = []  # 곡괭이 별 피로도 저장 리스트
  for i in range(0, len(minerals), 5):
    t.append(compare(minerals[i:i+5]))
  t = sorted(t, key=lambda x : x[2], reverse=True)

  idx, midx = 0, 0
  while True:
    if midx > len(t)-1 or sum(picks) == 0:
      break
    
    if picks[idx] != 0:
      picks[idx] -= 1
      answer += t[midx][idx]
    else:
      idx += 1
      continue
    midx += 1
    
  return answer  

# Solution By Others
def others(picks, minerals):
    def solve(picks, minerals, fatigue):
        if sum(picks) == 0 or len(minerals) == 0:
            return fatigue
        result = [float('inf')]
        for i, fatigues in enumerate(({"diamond": 1, "iron": 1, "stone": 1},
                                      {"diamond": 5, "iron": 1, "stone": 1},
                                      {"diamond": 25, "iron": 5, "stone": 1},)):
            if picks[i] > 0:
                next_picks = picks.copy()
                next_picks[i] -= 1
                next_fatigue = fatigue + sum(fatigues[mineral] for mineral in minerals[:5])
                result.append(solve(next_picks, minerals[5:], next_fatigue))
        return min(result)

    return solve(picks, minerals, 0)