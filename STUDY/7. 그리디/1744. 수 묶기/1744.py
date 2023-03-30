import sys
input=sys.stdin.readline

def solution(n):
    plus,minus,amb,rest,result=[],[],[],[],[]
    plen,mlen=0,0
    for _ in range(n):
        value=int(input())
        if value>1:
            plus+=[value]
            plen+=1
        elif value>=0: amb+=[value]
        else:
            minus+=[value]
            mlen+=1

    plus.sort(reverse=True)
    minus.sort()

    for i in range(0,plen,2):
        if i==plen-1:
            result+=[plus[i]]
            break
        result+=[plus[i]*plus[i+1]]

    for i in range(0,mlen,2):
        if i==mlen-1:
            rest+=[minus[i]]
            break
        result+=[minus[i]*minus[i+1]]

    if rest:
        if 0 not in amb:
            result+=[rest.pop()]

    if amb:
        result+=amb

    return sum(result)

print(solution(int(input())))