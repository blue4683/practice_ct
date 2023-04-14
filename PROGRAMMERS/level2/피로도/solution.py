def dfs(cnt,k,visited,dungeons,n):
    global answer
    
    if cnt>answer:
        answer=cnt
        
    for i in range(n):
        if not visited[i] and k>=dungeons[i][0]:
            visited[i]=1
            dfs(cnt+1,k-dungeons[i][1],visited,dungeons,n)
            visited[i]=0
    
def solution(k, dungeons):
    global answer
    answer = 0
    n=len(dungeons)
    visited=[0]*n
    dfs(0,k,visited,dungeons,n)
    return answer