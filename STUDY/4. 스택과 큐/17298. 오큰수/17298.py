import sys
input = sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
stack=[]
result=[-1]*n
for i in range(n):
    while stack and arr[stack[-1]]<arr[i]:
        result[stack.pop()]=arr[i]
    stack.append(i)
print(*result)
# 2차
# def search(st,ed,v):
#     for j in range(st,ed):
#         if v<arr[j]:
#             tmp=(j,arr[j])
#             stack.append(tmp)
#             result.append(tmp[1])
#             return
#     else:
#         result.append(-1)
#     return

# n=int(input())
# arr=list(map(int,input().split()))
# stack=deque([])
# result=[]
# for idx in range(n):
#     value=arr[idx]
#     if not stack:
#         search(idx+1,n,value)
#         continue
#     while stack:
#         tmp=stack.popleft()
#         if tmp[0]<idx:
#             continue
#         else:
#             if tmp[1]>value:
#                 for j in range(idx+1,tmp[0]):
#                     if value<arr[j]:
#                         stack.append((j,arr[j]))
#                         result.append(arr[j])
#                         break
#                 else:
#                     result.append(tmp[1])
#                 stack.appendleft(tmp)
#                 break
#     else:
#         search(idx+1,n,value)
#         continue
# print(*result)


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