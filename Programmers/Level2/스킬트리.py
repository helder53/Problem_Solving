# My Solution
def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        idx = 0
        for j in i:
            if j in skill and j != skill[idx]:
                break
            elif j in skill and j == skill[idx]:
                idx += 1

        else:
            answer += 1
    return answer
  
# Solution By Others
def others(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer