# My Solution
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(1, total+1):
        if (total / i) % 1 == 0:
            a = total / i
            
            if a >= i:
                if (2*a) + (2*i) == (brown + 4):
                    return [a, i]
    return answer

# Solution By Others
def others(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]