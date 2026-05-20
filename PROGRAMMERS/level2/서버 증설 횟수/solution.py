from collections import deque


def solution(players, m, k):
    answer = 0
    server = deque()
    for t, cnt in enumerate(players):
        while server and t - server[0] >= k:
            server.popleft()
            
        if (cnt // m) > len(server):
            for _ in range((cnt // m) - len(server)):
                server.append(t)
                answer += 1
        
    return answer
