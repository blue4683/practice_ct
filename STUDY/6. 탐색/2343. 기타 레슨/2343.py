import sys
input=sys.stdin.readline

n,m=map(int,input().split())
lessons=list(map(int,input().split()))
s,e=0,0

for lesson in lessons:
    if s<lesson: s=lesson
    e+=lesson

while s<=e:
    mid=(s+e)//2
    time=0
    cnt=0
    for i in range(n):
        if time+lessons[i]>mid:
            cnt+=1
            time=0
        time+=lessons[i]
    if time: cnt+=1
    if cnt>m: s=mid+1
    else: e=mid-1

print(s)

# import sys
# input=sys.stdin.readline

# def dfs(depth,cp,st):
#     global result
#     if depth==m-1:
#         cp=[0]+cp+[n]
#         time=[]
#         max_time=0
#         for i in range(1,m+1):
#             tmp=sum(lessons[cp[i-1]:cp[i]])
#             if tmp>result: return
#             if tmp>max_time: max_time=tmp
#             time+=[tmp]
#         result=min(result,max_time)
#         return

#     for i in range(st,n-1):
#         if not visited[i]:
#             visited[i]=1
#             dfs(depth+1,cp+[i],i)
#             visited[i]=0

# n,m=map(int,input().split())
# lessons=list(map(int,input().split()))
# visited=[0]*n
# result=1e9
# dfs(0,[],1)
# print(result)