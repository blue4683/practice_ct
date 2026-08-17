from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    INF = 10 ** 9
    answer = [INF, INF]
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    summits = set(summits)
    def dijkstra():
        dists = [INF] * (n + 1)
        heap = []
        for gate in gates:
            dists[gate] = 0
            heappush(heap, (0, gate))

        while heap:
            dist, now = heappop(heap)
            if dist > dists[now]:
                continue
                
            for node, d in graph[now]:
                if dists[node] <= max(dists[now], d):
                    continue
                    
                dists[node] = max(dists[now], d)
                if node not in summits:
                    heappush(heap, (dists[node], node))
        
        return dists
    
    dists = dijkstra()
    for summit in sorted(summits):
        if dists[summit] < answer[1]:
            answer = [summit, dists[summit]]
    
    return answer
