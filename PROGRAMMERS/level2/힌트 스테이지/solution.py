def solution(cost, hint):
    INF = 10 ** 9
    answer = INF
    n = len(cost)

    def dfs(depth, value, hints):
        nonlocal answer
        if value >= answer:
            return

        if depth == n:
            answer = min(answer, value)
            return

        cnt = min(hints[depth + 1], n - 1)
        dfs(depth + 1, value + cost[depth][cnt], hints)
        if depth < n - 1:
            c, *arr = hint[depth]
            for i in arr:
                hints[i] += 1

            dfs(depth + 1, value + cost[depth][cnt] + c, hints)
            for i in arr:
                hints[i] -= 1

    dfs(0, 0, {i: 0 for i in range(1, n + 1)})
    return answer
