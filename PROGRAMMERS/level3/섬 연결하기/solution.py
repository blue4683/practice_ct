def find(x):
    if graph[x] != x:
        return find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        graph[x] = y
    else:
        graph[y] = x


def solution(n, costs):
    global graph

    answer = 0
    graph = [i for i in range(n + 1)]
    costs.sort(key=lambda x: x[-1])

    for x, y, cost in costs:
        if find(x) != find(y):
            union(x, y)
            answer += cost

    return answer
