n = int(input())
if n == 1:
    print(0)
    
else:
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    for node, parent in enumerate(arr, 1):
        graph[parent].append(node)
        
    print(*map(len, graph[1:]))
