import sys
input=sys.stdin.readline

n=int(input())
p=sorted(list(map(int,input().split())))
for idx in range(1,n):
    p[idx]+=p[idx-1]
print(sum(p))