import sys
input = sys.stdin.readline


def dfs(depth, now, visited, root):
    global scores
    if 0 not in visited:
        scores[root] = max(visited)

    for friend in graph[now]:
        if visited[friend] and visited[friend] <= depth:
            continue

        visited[friend] = depth
        dfs(depth + 1, friend, visited, root)


n = int(input())
m = 0
graph = [[] for _ in range(51)]
while 1:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break

    graph[a].append(b)
    graph[b].append(a)
    m = max(m, a, b)

scores = [10 ** 9] * (m + 1)
for i in range(m + 1):
    if not graph[i]:
        continue

    visited = [0] * (m + 1)
    visited[0] = 1
    visited[i] = 1
    dfs(1, i, visited, i)

score = min(scores)
cnt = scores.count(score)

print(score, cnt)
for i in range(1, m + 1):
    if scores[i] == score:
        print(i, end=" ")
