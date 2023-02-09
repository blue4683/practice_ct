import sys
input = sys.stdin.readline

n,m=map(int,input().split())
sum_arr=[[0]*(n+1) for _ in range(n+1)]
arr = [[0]*(n+1)]
for i in range(n):
    a = [0]+list(map(int,input().split()))
    arr.append(a)

for x in range(1,n+1):
    for y in range(1,n+1):
        sum_arr[x][y]=sum_arr[x-1][y]+sum_arr[x][y-1]-sum_arr[x-1][y-1]+arr[x][y]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(sum_arr[x2][y2]-sum_arr[x1-1][y2]-sum_arr[x2][y1-1]+sum_arr[x1-1][y1-1])