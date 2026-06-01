from collections import defaultdict


def solution(edges):
    answer = []
    indegree, outdegree = defaultdict(int), defaultdict(int)
    max_num = 0
    for a, b in edges:
        outdegree[a] += 1
        indegree[b] += 1
        max_num = max(max_num, a, b)

    node, donut, stick, eight = 0, 0, 0, 0
    for i in range(1, max_num + 1):
        if outdegree[i] >= 2 and not indegree[i]:
            node = i

        if outdegree[i] >= 2 and indegree[i]:
            eight += 1

        if not outdegree[i] and indegree[i]:
            stick += 1

    donut = max(0, outdegree[node] - stick - eight)
    answer = [node, donut, stick, eight]
    return answer
