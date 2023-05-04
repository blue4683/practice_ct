import sys
input=sys.stdin.readline
    
n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]
value=[0]*(k+1)
value[0]=1
for coin in coins:
    for i in range(1,k+1):
        if i<coin: continue
        value[i]=value[i]+value[i-coin]
print(value[k])