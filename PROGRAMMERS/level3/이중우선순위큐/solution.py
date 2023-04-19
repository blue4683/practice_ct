from heapq import *
def solution(operations):
    answer = []
    n=len(operations)
    visited=[0]*n
    max_heap=[]
    min_heap=[]
    for i in range(n):
        order,num=operations[i].split()
        num=int(num)
        if order=='I':
            visited[i]=1
            heappush(max_heap,(-num,i))
            heappush(min_heap,(num,i))
        else:
            if num==1:
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]]=0
                    heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]]=0
                    heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)
        
    MAX,MIN=0,0
    if max_heap:
        MAX=-max_heap[0][0]
    if min_heap:
        MIN=min_heap[0][0]
    answer=[MAX,MIN]
    return answer