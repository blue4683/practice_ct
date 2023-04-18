import sys
input=sys.stdin.readline

n,c=map(int,input().split())
houses=sorted([int(input()) for _ in range(n)])
start,end=1,houses[-1]-houses[0]
result=0
while start<=end:
    mid=(start+end)//2
    now=houses[0]
    cnt=1
    for i in range(1,n):
        if houses[i]>=now+mid:
            cnt+=1
            now=houses[i]
    if cnt>=c:
        start=mid+1
        result=mid
    else:
        end=mid-1
print(result)