import sys
input = sys.stdin.readline

n=int(input())
numList=set(map(int, input().split()))
m=int(input())
targetList=list(map(int,input().split()))

for target in targetList:
    if target in numList:
        print(1)
    else:
        print(0)