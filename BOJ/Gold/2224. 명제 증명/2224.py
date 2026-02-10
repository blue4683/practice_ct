import sys
input = sys.stdin.readline


n = int(input())
graph = [[0] * 58 for _ in range(58)]
for _ in range(n):
    p, _, q = input().split()
    graph[ord(p) - ord('A')][ord(q) - ord('A')] = 1

for mid in range(58):
    for s in range(58):
        for e in range(58):
            if not graph[s][e] and graph[s][mid] and graph[mid][e]:
                graph[s][e] = 1

result = []
for s in range(58):
    for e in range(58):
        if graph[s][e] and s != e:
            result.append((chr(ord('A') + s), '=>', chr(ord('A') + e)))

print(len(result))
for res in result:
    print(*res)
