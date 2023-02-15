import sys
from collections import deque
input = sys.stdin.readline

# 1차
# def search(value,idx):
#     for j in range(idx+1,n):
#         if value<arr[j]:
#             return (j,arr[j])
#     else:
#         return -1

# n=int(input())
# arr=list(map(int,input().split()))
# stack=deque([])
# result=[]
# for idx in range(n):
#     value=arr[idx]
#     while stack:
#         if stack[0][0]<=idx:
#             stack.popleft()
#         else:
#             break
#     if not stack:
#         nge=search(value,idx)
#         if nge==-1:
#             result.append(nge)
#             continue
#         else:
#             stack.append(nge)
#             result.append(nge[1])
#             continue
#     else:
#         for s in stack:
#             if s[1]>value:
#                 result.append(s[1])
#                 break
#             else:
#                 pass
#         else:
#             nge=search(value,idx)
#             if nge==-1:
#                 result.append(nge)
#                 continue
#             else:
#                 stack.append(nge)
#                 result.append(nge[1])
#                 continue
# print(*result)