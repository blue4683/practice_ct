import sys
input=sys.stdin.readline
INF=float('inf')

def ccw(a,b,c):
    x1,y1=a
    x2,y2=b
    x3,y3=c
    return (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)

def convexHull():
    stack=[]
    for next in pos:
        while len(stack)>=2:
            first,second=stack[-2],stack[-1]
            if ccw(first,second,next)>0:
                break
            stack.pop()
        stack.append(next)
    return stack

n=int(input())
answer=-2
pos=[list(map(int,input().split())) for _ in range(n)]
pos.sort(key=lambda x:(x[1],x[0]))
answer+=len(convexHull())
pos.reverse()
answer+=len(convexHull())
print(answer)