'''
1. 시작부터 x만큼은 값이 다르면 안됨
2. 값이 달라진 시점부터 x만큼 값이 같아야함
3. 내리막길 설치 후 바로 오르막길이면 안됨
4. 값이 달라진 시점부터 x만큼 갈 수 없으면 안됨
5. 
'''

def check(idx):
    row,col=[],[]
    for i in range(n):
        row+=[arr[idx][i]]
        col+=[arr[i][idx]]
    cnt=ispossible(row)+ispossible(col)
    return cnt

def ispossible(lst):
    cnt=1
    for i in range(1,n):
        if lst[i]==lst[i-1]: cnt+=1
        elif lst[i]-lst[i-1]==1 and cnt>=x: cnt=1
        elif lst[i]-lst[i-1]==-1 and cnt>=0: cnt=-x+1
        else:
            return 0
    if cnt>=0:
        return 1
    return 0

for testcase in range(1,int(input())+1):
    n,x=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    result=0
    for idx in range(n):
        result+=check(idx)
    print(f'#{testcase} {result}')