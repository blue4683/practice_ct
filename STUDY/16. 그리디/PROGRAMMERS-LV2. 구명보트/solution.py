def solution(people, limit):
    answer = 0
    l,r=0,len(people)-1
    arr=sorted(people)
    
    while l<=r:
        lh,rh=arr[l],arr[r]
        if lh+rh<=limit:
            l+=1
            r-=1
        else: r-=1
        answer+=1
    
    return answer