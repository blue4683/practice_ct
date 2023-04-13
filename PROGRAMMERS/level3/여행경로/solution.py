def dfs(depth,now,visited,tickets,n,result):
    global answer
    if depth==n:
        answer=result
        return
    for i in range(n):
        if not visited[i]:
            s,e=tickets[i]
            if s==now:
                visited[i]=1
                dfs(depth+1,e,visited,tickets,n,result+[e])
                visited[i]=0

def solution(tickets):
    global answer
    answer = []
    tickets.sort(key=lambda x:x[-1],reverse=True)
    n=len(tickets)
    visited=[0]*n
    dfs(0,'ICN',visited,tickets,n,['ICN'])
    return answer