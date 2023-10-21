import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
result=arr[:]

for i in range(1,n):
    result[i]=max(result[i],result[i-1]+arr[i])

print(max(result))