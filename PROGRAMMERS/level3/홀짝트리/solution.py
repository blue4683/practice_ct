def solution(nodes, edges):
    answer = [0, 0]
    nodes.sort()
    parent = [i for i in range(nodes[-1] + 1)]

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])

        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x < y:
            parent[x] = y

        else:
            parent[y] = x

    cnt = [0] * (nodes[-1] + 1)
    for x, y in edges:
        union(x, y)
        cnt[x] += 1
        cnt[y] += 1

    forest = set()
    odd = [[0] * (nodes[-1] + 1) for _ in range(2)]
    for node in nodes:
        x = find(node)
        forest.add(x)
        odd[int((node % 2) != (cnt[node] % 2))][x] += 1

    for x in forest:
        if odd[0][x] == 1:
            answer[0] += 1

        if odd[1][x] == 1:
            answer[1] += 1

    return answer
