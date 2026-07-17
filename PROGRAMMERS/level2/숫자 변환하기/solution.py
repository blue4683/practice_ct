from collections import defaultdict, deque


def solution(x, y, n):
    answer = -1
    q = deque([x])
    visited = defaultdict(lambda: 10 ** 9)
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == y:
            return visited[x] - 1
        
        for i, dx in enumerate([n, 2, 3]):
            if i == 0:
                xx = x + dx
                
            else:
                xx = x * dx

            if xx <= y and visited[xx] > visited[x] + 1:
                visited[xx] = visited[x] + 1
                q.append(xx)
        
    return answer
