import sys
input = sys.stdin.readline


t, a, b = map(int, input().split())
visited = [[0] * 2 for _ in range(t + 1)]
result = -1

visited[0][0] = 1
q = [(0, 0)]
while q:
    f, water = q.pop()
    result = max(result, f)
    if f + a <= t and not visited[f + a][water]:
        q.append((f + a, water))
        visited[f + a][water] = 1

    if f + b <= t and not visited[f + b][water]:
        q.append((f + b, water))
        visited[f + b][water] = 1

    if not water and not visited[f // 2][1]:
        q.append((f // 2, 1))
        visited[f // 2][1] = 1

print(result)
