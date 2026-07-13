def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin, row_end + 1):
        s = sum(map(lambda x: x % i, data[i - 1]))
        answer ^= s
        
    return answer
