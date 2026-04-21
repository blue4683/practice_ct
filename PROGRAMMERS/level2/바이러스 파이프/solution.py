def solution(n, infection, edges, k):
    answer = 0
    infected = {infection}
    graph = [[] for _ in range(n + 1)]
    for a, b, typ in edges:
        graph[a].append((b, typ))
        graph[b].append((a, typ))

    def dfs(depth, state, before):
        nonlocal answer
        if depth == k:
            answer = max(answer, len(state))
            return

        for typ in range(1, 4):
            if typ == before:
                continue

            used = set()
            q = [*state]
            visited = [0] * (n + 1)
            while q:
                x = q.pop()
                visited[x] = 1
                for xx, t in graph[x]:
                    if t != typ or visited[xx]:
                        continue

                    q.append(xx)
                    if xx not in state:
                        used.add(xx)

            dfs(depth + 1, state | used, typ)

    dfs(0, infected, 0)
    return answer
