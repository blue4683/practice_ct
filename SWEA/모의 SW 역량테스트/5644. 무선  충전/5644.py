def move(start):
    q=start
    time=0
    while 1:
        human1,human2=q.pop()
        possible1,possible2=[],[]
        for key in dic:
            if human1 in dic[key]:
                possible1+=[key]
            if human2 in dic[key]:
                possible2+=[key]
        if not possible1 and not possible2: pass
        else: check(possible1,possible2)
        if time==m: return
        a,b=move_a[time],move_b[time]
        x1,y1,x2,y2=*human1,*human2
        xx1,yy1,xx2,yy2=x1+dx[a],y1+dy[a],x2+dx[b],y2+dy[b]
        q+=[[[xx1,yy1],[xx2,yy2]]]
        time+=1

def check(pos1,pos2):
    global charge
    if not pos1:
        charge+=bc[pos2[0]][-1]
        return
    if not pos2:
        charge+=bc[pos1[0]][-1]
        return
    if pos1!=pos2 and len(pos1)==1 and len(pos2)==1:
        charge+=bc[pos1[0]][-1]+bc[pos2[0]][-1]
    elif pos1==pos2 and len(pos1)==1:
        charge+=bc[pos1[0]][-1]
    elif len(pos1)>=2 and len(pos2)<2:
        if pos1[0]==pos2[0]:
            charge+=bc[pos1[1]][-1]+bc[pos2[0]][-1]
        else:
            charge+=bc[pos1[0]][-1]+bc[pos2[0]][-1]
    elif len(pos2)>=2 and len(pos1)<2:
        if pos1[0]==pos2[0]:
            charge+=bc[pos1[0]][-1]+bc[pos2[1]][-1]
        else:
            charge+=bc[pos1[0]][-1]+bc[pos2[0]][-1]
    else:
        if pos1[0]!=pos2[0]:
            charge+=bc[pos1[0]][-1]+bc[pos2[0]][-1]
        else:
            if pos1[1]<pos2[1]:
                charge+=bc[pos1[1]][-1]+bc[pos2[0]][-1]
            else:
                charge+=bc[pos1[0]][-1]+bc[pos2[1]][-1]
    return

dx=[0,0,1,0,-1]
dy=[0,-1,0,1,0]

for testcase in range(1,int(input())+1):
    size=10
    arr=[[[0] for _ in range(size)] for _ in range(size)]
    start=[[[0,0],[9,9]]]
    m,a=map(int,input().split())
    move_a=list(map(int,input().split()))
    move_b=list(map(int,input().split()))
    bc=[list(map(int,input().split())) for _ in range(a)]
    bc=sorted(bc,key=lambda x:x[-1],reverse=True)
    dic={i:[] for i in range(a)}
    for i,v in enumerate(bc):
        bx,by,c,p=v
        for y in range(size):
            for x in range(size):
                if abs(bx-1-x)+abs(by-1-y)<=c:
                    dic[i]+=[[x,y]]
    charge=0
    move(start)
    print(f'#{testcase} {charge}')