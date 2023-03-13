d=[[0,0.5],[0,-0.5],[-0.5,0],[0.5,0]]

for testcase in range(1,int(input())+1):
    n=int(input())
    atoms=[list(map(int,input().split())) for _ in range(n)]
    result=0
    while len(atoms)>1:
        for i in range(len(atoms)):
            x,y,dir,k=atoms[i]
            xx,yy=x+d[dir][0],y+d[dir][1]
            atoms[i]=[xx,yy,dir,k]
        pos={}
        for atom in atoms:
            try: pos[(atom[0],atom[1])]+=[atom]
            except: pos[(atom[0],atom[1])]=[atom]
        atoms=[]
        for p in pos:
            if len(pos[p])>1:
                for atom in pos[p]:
                    result+=atom[-1]
            else:
                if -1000<=pos[p][0][0]<=1000 and -1000<=pos[p][0][1]<=1000:
                    atoms+=[pos[p][0]]
    print(f'#{testcase} {result}')