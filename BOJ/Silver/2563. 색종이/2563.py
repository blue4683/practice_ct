import sys
input = sys.stdin.readline

n=int(input())
paper=[[0]*100 for _ in range(100)]
for _ in range(n):
    w,h=map(int,input().split())
    for y in range(h,h-10,-1):
        for x in range(w,w+10):
            paper[y][x]=1
area=0
for y in range(100):
    for x in range(100):
        if paper[y][x]:
            area+=1
print(area)