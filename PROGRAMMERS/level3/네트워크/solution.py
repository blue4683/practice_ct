def init(n):
    graph = [i for i in range(n)]
    return graph

def find(x):
    global graph
    if x != graph[x]:
        return find(graph[x])
    return graph[x]

def union(a, b):
    global graph
    a, b = find(a), find(b)
    if a > b:
        graph[a] = b
    else:
        graph[b] = a

def solution(n, computers):
    global graph
    answer = n
    graph = init(n)
    for y in range(n):
        for x in range(n):
            if computers[y][x]:
                if find(y) != find(x):
                    union(x, y)
                    answer -= 1
    return answer