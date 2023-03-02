import heapq
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    heap=[]
    max_heap=[]
    k=int(input())
    visited=[0]*(k+1)
    for i in range(k):
        o,n=input().split()
        if o=='I':
            heapq.heappush(heap,(int(n),i))
            heapq.heappush(max_heap,(-int(n),i))
            visited[i]=1
        else:
            if heap:
                if n=='1':
                    while max_heap and not visited[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    if max_heap:
                        visited[max_heap[0][1]]=0
                        heapq.heappop(max_heap)
                else:
                    while heap and not visited[heap[0][1]]:
                        heapq.heappop(heap)
                    if heap:
                        visited[heap[0][1]]=0
                        heapq.heappop(heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while heap and not visited[heap[0][1]]:
        heapq.heappop(heap)
    if heap:
        print(-max_heap[0][0],heap[0][0])
    else:
        print('EMPTY')

# 2차
# for _ in range(int(input())):
#     heap=[]
#     max_heap=[]
#     for _ in range(int(input())):
#         o,n=input().split()
#         if o=='I':
#             heapq.heappush(heap,int(n))
#             heapq.heappush(max_heap,-int(n))
#         else:
#             if heap:
#                 if n=='1':
#                     max_value=-heapq.heappop(max_heap)
#                     heap.remove(max_value)
#                 else:
#                     min_value=-heapq.heappop(heap)
#                     max_heap.remove(min_value)
#     if heap:
#         print(-heapq.heappop(max_heap),heapq.heappop(heap))
#     else:
#         print('EMPTY')

# 1차
# class Heap:
#     def __init__(self):
#         self.heap=[]
#         self.heap.append(1e9)

#     def check_swap_up(self,idx):
#         if idx<=1:
#             return False
#         parent_idx=idx//2
#         return True if self.heap[idx]>self.heap[parent_idx] else False
    
#     def insert(self,node):
#         self.heap.append(node)
#         idx=len(self.heap)-1

#         while self.check_swap_up(idx):
#             parent_idx=idx//2
#             self.heap[idx],self.heap[parent_idx]=self.heap[parent_idx],self.heap[idx]
#             idx=parent_idx
#         return True
    
#     def check_swap_down(self,idx):
#         left_idx=idx*2
#         right_idx=idx*2+1

#         if left_idx>=len(self.heap):
#             return False
        
#         elif right_idx>=len(self.heap):
#             if self.heap[left_idx]>self.heap[idx]:
#                 self.flag=1
#                 return True
#             else:
#                 return False
#         else:
#             if self.heap[left_idx]>self.heap[right_idx]:
#                 if self.heap[left_idx]>self.heap[idx]:
#                     self.flag=1
#                     return True
#                 else:
#                     return False
#             else:
#                 if self.heap[right_idx]>self.heap[idx]:
#                     self.flag=2
#                     return True
#                 else:
#                     return False
    
#     def pop(self,n):
#         if len(self.heap)<=1:
#             return
#         if len(self.heap)==2:
#             return self.heap.pop()
#         if n==-1:
#             max=self.heap[0]
#             for i in range(len(self.heap)//2,len(self.heap)):
#                 if self.heap[i]<max:
#                     max=self.heap[i]
#                     idx=i
#             if idx!=len(self.heap)-1:
#                 self.heap[idx]=self.heap.pop()
#             else:
#                 return self.heap.pop()
#         else:
#             max=self.heap[1]
#             self.heap[1]=self.heap.pop()
#             idx=1

#         self.flag=0
#         while self.check_swap_down(idx):
#             left_idx=idx*2
#             right_idx=idx*2+1

#             if self.flag==1:
#                 self.heap[idx],self.heap[left_idx]=self.heap[left_idx],self.heap[idx]
#             elif self.flag==2:
#                 self.heap[idx],self.heap[right_idx]=self.heap[right_idx],self.heap[idx]
#         return max
    
# for _ in range(int(input())):
#     heap=Heap()
#     for _ in range(int(input())):
#         o,n=input().split()
#         if o=='I':
#             heap.insert(int(n))
#         else:
#             heap.pop(int(n))
#     if len(heap.heap)<=1:
#         print('EMPTY')
#     else:
#         print(heap.heap[1],heap.pop(-1))