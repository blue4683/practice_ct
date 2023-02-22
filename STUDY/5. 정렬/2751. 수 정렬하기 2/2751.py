import sys
input=sys.stdin.readline

def mergesort(arr):
    if len(arr)<2:
        return arr
    pivot=len(arr)//2
    low=mergesort(arr[:pivot])
    high=mergesort(arr[pivot:])
    l,h=0,0
    merge=[]
    while l<len(low) and h<len(high):
        if low[l]<high[h]:
            merge+=[low[l]]
            l+=1
        else:
            merge+=[high[h]]
            h+=1
    merge+=low[l:]
    merge+=high[h:]
    return merge

n=int(input())
arr=[int(input()) for _ in range(n)]
arr=mergesort(arr)
for value in arr:
    print(value)