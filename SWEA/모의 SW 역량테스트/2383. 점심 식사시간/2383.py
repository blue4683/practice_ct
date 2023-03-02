''' 1차
def dfs(time,arr1,arr2,visited):
    global result
    if time>=result:
        return

    arr1=list(map(lambda x:x-1 if x>0 else 0, arr1))
    arr2=list(map(lambda x:x-1 if x>0 else 0, arr2))
    
    if set(visited)=={1} and arr1==[0]*3 and arr2==[0]*3:
        result=min(time,result)
        return
    tmp1,tmp2,tmp3=arr1,arr2,visited
    for i in range(len(distance)):
        if not visited[i]:
            da,db=distance[i]
            sa,sb=map(lambda x:x[-1],stair)
            if 0 not in arr1: pass
            elif da>time: pass
            else:
                visited[i]=1
                idx=arr1.index(0)
                if da==time:
                    arr1[idx]=sa+1
                    # dfs(time+1,arr1,arr2)
                else:
                    arr1[idx]=sa
                    # dfs(time+1,arr1,arr2)
                # arr1[idx]=0
                # visited[i]=0

            if 0 not in arr2: pass
            elif db>time: pass
            else:
                visited[i]=1
                idx=arr2.index(0)
                if db==time:
                    arr2[idx]=sb+1
                    # dfs(time+1,arr1,arr2)
                else:
                    arr2[idx]=sb
                    # dfs(time+1,arr1,arr2)
                # arr2[idx]=0
                # visited[i]=0
    dfs(time+1,arr1,arr2,visited)
    arr1,arr2,visited=tmp1,tmp2,tmp3

for testcase in range(1,int(input())+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    people=[]
    stair=[]
    for y in range(n):
        for x in range(n):
            if arr[y][x]==1:
                people+=[[y,x]]
            if arr[y][x]>1:
                stair+=[[y,x,arr[y][x]]]
    visited=[0]*len(people)
    distance=[]
    for y,x in people:
        tmp=[]
        for b,a,_ in stair:
            tmp+=[abs(b-y)+abs(a-x)]
        distance+=[tmp]
    result=1e9
    dfs(0,[0]*3,[0]*3,visited)
    print(f'#{testcase} {result}')
'''
# 2차
from collections import deque

def select(depth):
    if depth==cnt:
        s1,s2=[],[]
        for i in range(cnt):
            da,db=distance[i]
            if not selected[i]:
                s1+=[da+1]
            else:
                s2+=[db+1]
        down(s1,s2)
        return

    for i in range(2):
        if not visited[depth]:
            visited[depth]=1
            selected[depth]=i
            select(depth+1)
            selected[depth]=0
            visited[depth]=0

def down(arr1,arr2):
    global result
    q1,q2=deque(sorted(arr1)),deque(sorted(arr2))
    wait1,wait2=deque([]),deque([])
    d1,d2=map(lambda x:x[-1],stair)
    time=0
    complete=0
    while complete!=cnt:
        time+=1
        while wait1:
            if wait1[0]==time:
                wait1.popleft()
                complete+=1
            else: break
        while wait2:
            if wait2[0]==time:
                wait2.popleft()
                complete+=1
            else: break
        while q1:
            if q1[0]==time and len(wait1)<3:
                wait1.append(q1.popleft()+d1)
            else: break
        while q2:
            if q2[0]==time and len(wait2)<3:
                wait2.append(q2.popleft()+d2)
            else: break
        if len(wait1)==3:
            for i in range(len(q1)):
                if q1[i]==time:
                    q1[i]+=1
        if len(wait2)==3:
            for i in range(len(q2)):
                if q2[i]==time:
                    q2[i]+=1
    result=min(time,result)

for testcase in range(1,int(input())+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    people=[]
    stair=[]
    for y in range(n):
        for x in range(n):
            if arr[y][x]>1:
                stair+=[[y,x,arr[y][x]]]
            if arr[y][x]==1:
                people+=[[y,x]]
    cnt=len(people)
    selected=[0]*cnt
    visited=[0]*cnt
    distance=[]
    for y,x in people:
        tmp=[]
        for b,a,_ in stair:
            tmp+=[abs(b-y)+abs(a-x)]
        distance+=[tmp]
    result=1e9
    select(0)
    print(f'#{testcase} {result}')