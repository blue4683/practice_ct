def solution(dist_limit, split_limit):
    answer = 1
    visited = {}

    def dfs(node, leaf, used, split):
        nonlocal answer
        if used > dist_limit:
            return

        state = (node, split)
        if state in visited and visited[state] <= used:
            return

        visited[state] = used
        answer = max(answer, node + leaf)
        for i in [2, 3]:
            if split * i > split_limit:
                continue

            children = node * i
            remain = dist_limit - used
            next_node = min(children, remain)
            next_leaf = leaf + children - next_node
            dfs(next_node, next_leaf, used + next_node, split * i)

    dfs(1, 0, 1, 1)
    return answer
