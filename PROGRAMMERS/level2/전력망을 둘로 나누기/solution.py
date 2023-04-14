def find(x):
    global graph
    if x!=graph[x]:
        return find(graph[x])
    return graph[x]

def union(a,b):
    global graph
    a,b=find(a),find(b)
    if a>b:
        graph[a]=b
    else:
        graph[b]=a

def solution(n, wires):
    global graph
    answer = 1e9
    wires.sort()
    for i in range(n):
        graph=[i for i in range(n+1)]
        case=wires[:i]+wires[i+1:]
        for a,b in case:
            if find(a)!=find(b):
                union(a,b)
        for i in range(1,n+1):
            graph[i]=find(i)
        answer=min(answer,abs(2*graph.count(1)-n))
    return answer