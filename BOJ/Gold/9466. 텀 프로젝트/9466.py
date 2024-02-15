import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


def dfs(now):
    global visited, result, students

    visited[now] = 1
    team.append(now)
    next = students[now]

    if visited[next]:
        if next in team:
            for num in team[team.index(next):]:
                result.add(num)
        return
    else:
        dfs(next)


for _ in range(int(input())):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    result = set()

    for i in range(1, n + 1):
        if visited[i] == 0:
            team = []
            dfs(i)

    print(n - len(result))
