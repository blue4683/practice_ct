from heapq import heappop, heappush


def solution(n, k, enemy):
    answer = 0
    v, block = 0, []
    for i in range(len(enemy)):
        if len(block) < k:
            heappush(block, enemy[i])
            
        else:
            if k and block[0] < enemy[i]:
                v += heappop(block)
                heappush(block, enemy[i])
        
            else:
                v += enemy[i]
                
            if v > n:
                answer = i
                break
    else:
        answer = len(enemy)
        
    return answer
