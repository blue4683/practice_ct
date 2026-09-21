from heapq import heappush, heappop


n = int(input())
min_heap, max_heap = [], []

for _ in range(n):
    x = int(input())
    if len(max_heap) == len(min_heap):
        heappush(max_heap, -x)
        
    else:
        heappush(min_heap, x)
    
    if min_heap and -max_heap[0] > min_heap[0]:
        a, b = -heappop(max_heap), heappop(min_heap)
        heappush(max_heap, -b)
        heappush(min_heap, a)
    
    print(-max_heap[0])
        