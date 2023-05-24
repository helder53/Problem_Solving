# My Solution
def f(n):
    x = ""
	
    while n > 0:
      n, mod = divmod( n, 2 )
      x += str(mod)

    return x[::-1]

def solution(s):
    cnt, result = 0, 0

    while(s!='1'):
        cnt += 1
        result += s.count('0')

        s = s.replace('0','')
        s = f(len(s))
    
    return [cnt, result]
  

# Solution By Others
def others(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]