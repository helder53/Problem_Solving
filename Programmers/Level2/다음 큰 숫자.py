# My Solution
def solution(n):
    binary = str(bin(n))[2:]
    if len(set(binary)) == 1 : return int('10' + binary[1:],2)
    one = binary.count('1')

    while(True):
        n += 1
        if str(bin(n))[2:].count('1') == one : return n
        
# Solution By Others
def others(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n