def solution(sizes):
    answer = 0
    n=len(sizes)
    for i in range(n):
        sizes[i]=sorted(sizes[i])
    max_w,max_h=0,0
    for w,h in sizes:
        max_w=max(w,max_w)
        max_h=max(h,max_h)
    answer=max_w*max_h
    return answer