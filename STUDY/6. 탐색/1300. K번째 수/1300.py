import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
s,e=1,k
result=0
while s<=e:
    mid=(s+e)//2
    cnt=0
    for i in range(1,n+1):
        cnt+=min(mid//i,n)
    if cnt<k:
        s=mid+1
    else:
        result=mid
        e=mid-1
print(result)

# import sys
# input=sys.stdin.readline

# n=int(input())
# k=int(input())
# cnt=0
# for i in range(n):
#     if cnt+1+2*(n-i-1)<k: cnt+=1+2*(n-i-1)
#     else:
#         for j in range(i,n):
#             cnt+=1
#             if i!=j:
#                 cnt+=1
#             if cnt>=k:
#                 print((i+1)*(j+1))
#                 exit()

# 1차
# import sys
# input=sys.stdin.readline

# n=int(input())
# k=int(input())
# arr=[]
# cnt=0
# flag=0
# for i in range(n):
#     for j in range(n):
#         cnt+=1
#         arr+=[(i+1)*(j+1)]
#         if cnt>int(1e9):
#             flag=1
#             break
#     if flag:
#         break
# arr.sort()
# print(arr[k])