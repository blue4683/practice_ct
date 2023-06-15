import sys
input=sys.stdin.readline

n=int(input())
cost=[list(map(int,input().split())) for _ in range(n)]
result=[[0]*3 for _ in range(n)]
result[0]=cost[0]

for i in range(1,n):
    result[i][0]=min(result[i-1][1],result[i-1][2])+cost[i][0]
    result[i][1]=min(result[i-1][0],result[i-1][2])+cost[i][1]
    result[i][2]=min(result[i-1][0],result[i-1][1])+cost[i][2]

print(min(result[n-1]))