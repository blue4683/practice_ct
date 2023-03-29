import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coins=[]
for _ in range(n):
    coins+=[int(input())]
coins.sort(reverse=True)
result=0
for coin in coins:
    r=k//coin
    result+=r
    k-=r*coin
    if not k: break
print(result)