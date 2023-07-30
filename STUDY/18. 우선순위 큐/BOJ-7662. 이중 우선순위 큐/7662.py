from heapq import *
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    k=int(input())
    dat=[0]*k
    min_heap,max_heap=[],[]
    for i in range(k):
        op,num=input().split()
        num=int(num)
        
        if op=='I':
            heappush(min_heap,[num,i])
            heappush(max_heap,[-num,i])
            dat[i]=1
            continue

        if num>0:
            while max_heap and dat[max_heap[0][1]]==0: heappop(max_heap)
            if max_heap:
                _,idx=heappop(max_heap)
                dat[idx]=0
        else:
            while min_heap and dat[min_heap[0][1]]==0: heappop(min_heap)
            if min_heap:
                _,idx=heappop(min_heap)
                dat[idx]=0
        
    while max_heap and dat[max_heap[0][1]]==0: heappop(max_heap)
    while min_heap and dat[min_heap[0][1]]==0: heappop(min_heap)

    print(*[-max_heap[0][0],min_heap[0][0]]) if max_heap else print('EMPTY')