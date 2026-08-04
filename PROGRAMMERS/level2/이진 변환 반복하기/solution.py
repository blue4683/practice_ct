def solution(s):
    answer = []
    cnt, zero = 0, 0
    while s != '1':
        cnt += 1
        zero += s.count('0')
        s = s.replace('0', '')
        x = len(s)
        s = bin(x)[2:]
        
    answer = [cnt, zero]
    return answer
