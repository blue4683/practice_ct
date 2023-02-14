# 1차 (시간초과)
# import sys
# input = sys.stdin.readline
# 
# N,L=map(int,input().split())
# A=list(map(int,input().split()))
# result=[A[0]]
# q=[(0,A[0])]
# for idx in range(1,N):
#     if q[0][0]<idx-L+1:
#         q.pop(0)
#     while True:
#         if not q:
#             q.append((idx,A[idx]))
#             break
#         if q[-1][1]>A[idx]:
#             q.pop()
#         else:
#             q.append((idx,A[idx]))
#             break
#     result.append(q[0][1])
# print(*result)

# 2차
from collections import deque
import sys
input = sys.stdin.readline

N,L=map(int,input().split())
A=list(map(int,input().split()))
result=[A[0]]
q=deque([(0,A[0])])
for idx in range(1,N):
    if q[0][0]<idx-L+1:
        q.popleft()
    while True:
        if not q:
            q.append((idx,A[idx]))
            break
        if q[-1][1]>A[idx]:
            q.pop()
        else:
            q.append((idx,A[idx]))
            break
    result.append(q[0][1])
print(*result)