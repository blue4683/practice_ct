def solution(n, l, r):
    answer = 0
    for i in range(l - 1, r):
        while i > 0:
            i, res = i // 5, i % 5
            if res == 2:
                break
                
        else:
            answer += 1
            
    return answer
