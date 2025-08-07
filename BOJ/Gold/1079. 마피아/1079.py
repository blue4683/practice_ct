import sys
input = sys.stdin.readline


def dfs(lived, alive, guilty):
    global result
    if alive == {mafia} or mafia not in alive:
        result = max(result, lived)
        return

    if len(alive) % 2:
        max_guilty = 0
        dead = -1
        for i in sorted(alive):
            if guilty[i] > max_guilty:
                max_guilty = guilty[i]
                dead = i

        dfs(lived, alive - {dead}, guilty)

    else:
        for i in alive:
            if i == mafia:
                continue

            dfs(lived + 1, alive - {i},
                [guilty[j] + arr[i][j] for j in range(n)])


n = int(input())
guilty = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
mafia = int(input())

result = 0
dfs(0, set(range(n)), guilty)
print(result)
