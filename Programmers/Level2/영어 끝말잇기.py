# My Solution
def solution(n, words):
    t = [0, 1]
    w = []
    check = True

    for i in range(len(words)):
        check = False
        t[0] += 1
        if t[0] > n:
            t[0] = 1
            t[1] += 1

        if w == []:
            w.append(words[i])
        else:
            
            if w[-1][-1] == words[i][0] and words[i] not in w:
                w.append(words[i])
            else:
                return t

    if check == False:
        return [0, 0]
      
# Solution By Others
def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]: return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]