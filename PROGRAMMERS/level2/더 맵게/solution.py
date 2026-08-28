from heapq import heappop, heappush, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville) > 1:
        x = heappop(scoville)
        if x >= K:
            break
        
        y = heappop(scoville)
        heappush(scoville, (x + 2 * y))
        answer += 1
        
    return answer if scoville[0] >= K else -1
