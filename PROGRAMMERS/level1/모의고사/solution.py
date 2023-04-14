def solution(answers):
    answer = []
    n=len(answers)
    p1=[i for i in range(1,6)]*(n//5+1)
    p2=[]
    for _ in range(n//8+2):
        for i in range(1,6):
            if i!=2:
                p2+=[2,i]
    p3=[]
    for _ in range(n//10+2):
        for i in [3,1,2,4,5]:
            p3+=[i,i]
    r1=sum(map(lambda x,y:int(x==y),answers,p1[:n]))
    r2=sum(map(lambda x,y:int(x==y),answers,p2[:n]))
    r3=sum(map(lambda x,y:int(x==y),answers,p3[:n]))
    r=max(r1,r2,r3)
    if r==r1:
        answer+=[1]
    if r==r2:
        answer+=[2]
    if r==r3:
        answer+=[3]
    return answer