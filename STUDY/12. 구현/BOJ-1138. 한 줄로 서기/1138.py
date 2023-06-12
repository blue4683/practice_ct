import sys
input=sys.stdin.readline

n=int(input())
result=[]
for idx in reversed(list(map(int,input().split()))):
    result.insert(idx,n)
    n-=1
print(*result)