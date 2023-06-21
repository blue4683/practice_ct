import sys
input=sys.stdin.readline

n=int(input())
consults=[list(map(int,input().split())) for _ in range(n)]
result=[0]*n

for i in range(n):
    t,p=consults[i]
    result[i]=max(result[i-1],result[i])
    if i+t<=n:
        result[i+t-1]=max(result[i+t-1],result[i-1]+p)

print(result[n-1])