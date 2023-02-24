import sys
input=sys.stdin.readline

def mergesort(start,end):
    global result
    if end-start<1:return
    mid=(start+end)//2
    mergesort(start,mid)
    mergesort(mid+1,end)
    for i in range(start,end+1):
        merge[i]=arr[i]
    k=start
    l,h=start,mid+1
    while l<=mid and h<=end:
        if merge[l]>merge[h]:
            arr[k]=merge[h]
            result+=(h-k)
            k+=1
            h+=1
        else:
            arr[k]=merge[l]
            k+=1
            l+=1
    while l<=mid:
        arr[k]=merge[l]
        k+=1
        l+=1
    while h<=end:
        arr[k]=merge[h]
        k+=1
        h+=1

n=int(input())
arr=[0]+list(map(int,input().split()))
merge=[0]*(n+1)
result=0
mergesort(1,n)
print(result)

# 2차
# n=int(input())
# arr=list(map(int,input().split()))
# result=0
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i]>arr[j]:result+=1
# print(result)

# 1차
# n=int(input())
# arr=list(map(int,input().split()))
# arr=list(map(tuple,enumerate(arr)))
# sorted_arr=sorted(arr,key=lambda x:x[1])
# dif=list(map(lambda x,y:y[0]-x[0],arr,sorted_arr))
# result=0
# print(dif)
# for d in dif:
#     if d>0:
#         result+=d
#     if d==0:
#         result+=1
# print(result)