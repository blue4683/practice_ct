import sys
input=sys.stdin.readline

def GCD(a,b):
    if a>b:
        tmp=a
        a=b
        b=tmp
    for _ in range(b):
        if not b%a:
            return a
        r=b%a
        b=a
        a=r

t=int(input())
for _ in range(t):
    a,b=map(int,input().rstrip().split())
    print(a*b//GCD(a,b))