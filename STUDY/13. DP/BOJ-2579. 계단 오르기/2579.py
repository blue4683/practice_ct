import sys
input=sys.stdin.readline

n=int(input())
stairs=[0]*301
for i in range(1,n+1): stairs[i]=int(input())
result=[0]*301
result[1]=stairs[1]
result[2]=sum(stairs[1:3])

for i in range(3,n+1):
    result[i]=max(result[i-3]+sum(stairs[i-1:i+1]),result[i-2]+stairs[i])

print(result[n])