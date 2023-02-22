def bingo():
    cnt=0
    for y in range(5):
        rcnt,ccnt=0,0
        for x in range(5):
            if visited[y][x]:
                rcnt+=1
            if visited[x][y]:
                ccnt+=1
        if rcnt==5:
            cnt+=1
        if ccnt==5:
            cnt+=1
    dcnt1=0
    dcnt2=0
    for z in range(5):
        if visited[z][z]:
            dcnt1+=1
        if visited[4-z][z]:
            dcnt2+=1
    if dcnt1==5:
        cnt+=1
    if dcnt2==5:
        cnt+=1
    return 1 if cnt>=3 else 0

def fill(n):
    for y in range(5):
        for x in range(5):
            if arr[y][x]==n:
                visited[y][x]=1
                return

arr=[list(map(int,input().split())) for _ in range(5)]
visited=[[0]*5 for _ in range(5)]
order=[]
for _ in range(5):
    order+=list(map(int,input().split()))
for idx in range(5*5):
    fill(order[idx])
    if bingo():
        print(idx+1)
        break