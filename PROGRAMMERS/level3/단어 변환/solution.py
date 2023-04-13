def dfs(depth, begin, target, words, visited):
    global answer
    if depth>=answer:
        return
    if begin==target:
        answer=min(depth,answer)
        return
    for i in range(len(words)):
        if not visited[i]:
            visited[i]=1
            word=words[i]
            cnt=sum(map(lambda x,y:int(x!=y),word,begin))
            if cnt==1:
                dfs(depth+1,word,target,words,visited)
            visited[i]=0

def solution(begin, target, words):
    global answer
    answer = 1e9
    visited = [0]*len(words)
    dfs(0, begin, target, words, visited)
    if answer == 1e9:
        answer = 0
    return answer