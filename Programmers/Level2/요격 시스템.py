# My Solution
def solution(targets):
    answer = 0
    targets.sort()
    a = targets[0]

    for i in range(1, len(targets)):
        if a[1] > targets[i][0]:
            a = [max(targets[i][0], a[0]), min(targets[i][1], a[1])]
        else:
            a = targets[i]
            answer += 1
    return answer

# Solution By Others
def others(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    answer = 0
    end = -1  # 마지막으로 요격한 미사일의 x좌표

    for s, e in targets:
        if s >= end:  # 이전에 요격한 미사일로는 현재 미사일을 요격할 수 없는 경우
            answer += 1
            end = e  # 현재 미사일을 요격함으로써 끝나는 지점을 업데이트

    return answer