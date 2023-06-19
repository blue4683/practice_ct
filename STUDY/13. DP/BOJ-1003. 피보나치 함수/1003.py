import sys
input=sys.stdin.readline

fib=[0]*42
fib[41]=1
fib[1]=1
for i in range(2, 41):
    fib[i]=fib[i-1]+fib[i-2]

t=int(input())

for _ in range(t):
    n=int(input())
    print(fib[n-1],fib[n])