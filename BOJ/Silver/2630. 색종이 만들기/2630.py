import sys
input=sys.stdin.readline

def slice(x1,y1,x2,y2):
    global white,blue
    l=x2-x1
    color=paper[y1][x1]
    if l<2:
        if color:
            blue+=1
        else:
            white+=1
        return
    for y in range(y1,y2):
        for x in range(x1,x2):
            if paper[y][x]!=color:
                slice(x1,y1,x1+l//2,y1+l//2)
                slice(x1+l//2,y1,x2,y1+l//2)
                slice(x1,y1+l//2,x1+l//2,y2)
                slice(x1+l//2,y1+l//2,x2,y2)
                return
    else:
        if color:
            blue+=1
        else:
            white+=1
    return

n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
white=0
blue=0
slice(0,0,n,n)
print(white)
print(blue)