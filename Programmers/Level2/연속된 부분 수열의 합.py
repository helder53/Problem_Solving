# My Solution
def solution(sequence, k):
    n = len(sequence)
    s = []
    start, end, sum_num = 0, 0, 0

    while end < n:
        sum_num += sequence[end]

        while sum_num > k and start <= end:
            sum_num -= sequence[start]
            start += 1
        
        if sum_num == k:
            s.append([start, end])
            sum_num -= sequence[start]
            start += 1
        
        end += 1

    return min(s, key=lambda x: x[1]-x[0])
  
# Solution By Others
def others(sequence, k):
    sdx, edx = 1, 1
    asdx, aedx = -1,-1
    ln = int(1e9)


    sequence = [0] + sequence
    prefix_sum = [0] * len(sequence)

    # prefix_sum 계산
    for i in range(1, len(sequence)):
        prefix_sum[i] = prefix_sum[i - 1] + sequence[i]

    # [0, 1, 3, 6, 10, 15]
    while sdx <= edx < len(sequence):
        check = prefix_sum[edx] - prefix_sum[sdx - 1]

        if check < k:
            edx += 1
        elif check == k:
            if ln > edx - sdx:
                ln = edx-sdx
                asdx, aedx = sdx, edx
            edx += 1
        else:
            sdx += 1


    return [asdx - 1, aedx - 1]