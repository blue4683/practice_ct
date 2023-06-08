n=int(input())
target=int(input())

d=[[1,0],[0,1],[-1,0],[0,-1]]

def make_snail(pos):
    global MAX, result
    y,x,dir=pos
    snail[y][x]=MAX
    if target==MAX:
        result=[y+1,x+1]
    MAX-=1

    for i in range(4):
        new_dir=(dir+i)%4
        dy,dx=d[new_dir]
        yy,xx=y+dy,x+dx
        if 0<=yy<n and 0<=xx<n and snail[yy][xx]==0:
            return [yy,xx,new_dir]

MAX=n**2
snail=[[0]*n for _ in range(n)]
pos=[0,0,0]
result=[]

while MAX:
    pos=make_snail(pos)

for line in snail:
    print(*line)
print(*result)