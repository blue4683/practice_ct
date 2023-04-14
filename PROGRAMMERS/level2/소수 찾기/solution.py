def dfs(depth,path,visited,numbers,n):
    global answer,num,case
    if path:
        case.add(int(path))
        
    if depth==n:
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i]=1
            dfs(depth+1,path+numbers[i],visited,numbers,n)
            dfs(depth+1,path,visited,numbers,n)
            visited[i]=0
        
def solution(numbers):
    global answer,num,case
    answer = 0
    LIMIT=int(1e7)+1
    num=[0]*LIMIT
    n=len(numbers)
    visited=[0]*n
    case=set()
    num[0]=1
    num[1]=1
    for i in range(2,LIMIT):
        if not num[i]:
            j=2
            while i*j<LIMIT:
                num[i*j]=1
                j+=1
    dfs(0,'',visited,numbers,n)
    for c in list(case):
        if not num[c]:
            answer+=1
    return answer