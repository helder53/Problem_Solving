# My Solution
def solution(topping):
    answer = 0

    a = set()
    b = {}

    for i in topping:
        b[str(i)] = b.get(str(i), 0)
        b[str(i)] += 1
    for i in topping:
        a.add(i)
        b[str(i)] -= 1
        if b[str(i)] == 0:
            del b[str(i)]
        if len(a) == len(b.keys()):
            answer += 1
    return answer


# Solution By Others
from collections import Counter

def others(topping):
    answer = 0
    be_ = set()
    af = Counter(topping)

    for t in topping:
        be_.add(t)
        af[t] -= 1

        if af[t] == 0:
            del af[t]
        if len(be_) == len(af):
            answer += 1

    return answer