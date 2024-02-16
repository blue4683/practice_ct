import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def check(team):
    q = [team.pop()]

    while q:
        x = q.pop()
        for node in graph[x]:
            if node in team:
                q.append(team.pop(team.index(node)))

    if team:
        return False
    else:
        return True


def seperate(a, b):
    global result
    if check(a[:]) and check(b[:]):
        a = sum(map(lambda x: population[x], a))
        b = sum(map(lambda x: population[x], b))
        if abs(a - b) < result:
            result = abs(a - b)
    return


n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    for j in info[1:]:
        graph[i].append(j)

result = 1e9

for i in range(1 << n):
    a, b = [], []
    for j in range(n):
        if i & (1 << j) != 0:
            a.append(j + 1)
        else:
            b.append(j + 1)

    if a and b:
        seperate(a, b)

print(result) if result != 1e9 else print(-1)
