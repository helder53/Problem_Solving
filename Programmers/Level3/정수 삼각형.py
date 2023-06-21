# My Solution
def solution(triangle):
    t = [[0 for j in i] for i in triangle]
    t[0][0] = triangle[0][0]
    

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):

            if j == 0:
                t[i][j] = t[i-1][j] + triangle[i][j]

            elif j == len(triangle[i])-1:
                t[i][j] = t[i-1][j-1] + triangle[i][j]

            else:
                a = t[i-1][j] + triangle[i][j]
                b = t[i-1][j-1] + triangle[i][j]

                t[i][j] = max(a, b)
    return max(max(t))

# Solution By Others
def others(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])