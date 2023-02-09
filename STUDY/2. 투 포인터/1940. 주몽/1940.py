import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = sorted(list(map(int,input().split())))
start=0
end=n-1
cnt=0
while start<end:
    value = arr[start]+arr[end]
    if value==m:
        cnt+=1
        start+=1
        end-=1
    elif value>m:
        end-=1
    else:
        start+=1
print(cnt)