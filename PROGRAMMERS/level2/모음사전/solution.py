alp=['A','E','I','O','U']

def dfs(depth,path,n):
    global case
    case+=[path]
    if depth==n:
        return
    for i in range(5):
        dfs(depth+1,path+alp[i],n)
        
def solution(word):
    global case
    answer = 0
    n=5
    case=[]
    dfs(0,'',n)
    answer=case.index(word)
    return answer