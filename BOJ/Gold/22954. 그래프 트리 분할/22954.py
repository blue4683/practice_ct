import sys
input = sys.stdin.readline


def travesal(node):
    visited[node] = 1
    edge_list = []
    node_list = [node]
    q = [node]

    while q:
        node = q.pop()
        for idx, next_node in graph[node]:
            if visited[next_node]:
                continue

            visited[next_node] = 1
            edge_list.append(idx)
            node_list.append(next_node)
            q.append(next_node)

    return edge_list, node_list, node


def solution():
    global graph, visited
    n, m = map(int, input().split())
    if n <= 2 or m <= n - 3:
        print(-1)
        return

    graph = [[] for _ in range(n + 1)]
    edge_list = []
    for i in range(1, m + 1):
        u, v = map(int, input().split())
        graph[u].append((i, v))
        graph[v].append((i, u))
        edge_list.append((i, u, v))

    visited = [0] * (n + 1)
    edges, nodes, last_nodes = [], [], []
    for node in range(1, n + 1):
        if visited[node]:
            continue

        edge, node, last_node = travesal(node)
        edges.append(edge)
        nodes.append(node)
        last_nodes.append(last_node)

    if len(nodes) > 2:
        print(-1)
        return

    if len(nodes) == 2:
        if len(nodes[0]) == len(nodes[1]):
            print(-1)
            return

        print(len(nodes[0]), len(nodes[1]))
        for i in range(2):
            print(*nodes[i])
            print(*edges[i])

        return

    edges, nodes, last_node = edges[0], nodes[0], last_nodes[0]
    new_edges = []
    for idx in edges:
        _, a, b = edge_list[idx - 1]
        if last_node in [a, b]:
            continue

        new_edges.append(idx)

    print(len(nodes) - 1, 1)
    print(*[node for node in nodes if node != last_node])
    print(*new_edges)
    print(last_node)
    print()


if __name__ == '__main__':
    solution()
