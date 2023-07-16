def solution(name):
    answer = 0
    cnt=list(map(lambda x:min(ord(x)-ord('A'),ord('Z')-ord(x)+1),name))
    answer+=sum(cnt)
    n=len(name)
    move=n-1
    
    for i in range(n):
        idx=i+1
        while idx<n and name[idx]=='A':
            idx+=1
            
        move=min(move,2*i+n-idx,2*(n-idx)+i)
        
    answer+=move
    
    return answer