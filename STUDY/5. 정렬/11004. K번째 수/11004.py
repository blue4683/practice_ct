import sys
input=sys.stdin.readline

def quicksort(s,e,k):
    global arr
    if s<e:
        pivot=partition(s,e)
        if pivot==k:
            return
        elif k<pivot:
            quicksort(s,pivot-1,k)
        else:
            quicksort(pivot+1,e,k)

def swap(i,j):
    global arr
    tmp=arr[i]
    arr[i]=arr[j]
    arr[j]=tmp

def partition(s,e):
    global arr

    if s+1==e:
        if arr[s]>arr[e]:
            swap(s,e)
        return e

    m=(s+e)//2
    swap(s,m)
    pivot=arr[s]
    i=s+1
    j=e
    while i<=j:
        while pivot<arr[j] and j>0:
            j-=1
        while pivot>arr[i] and i<len(arr)-1:
            i+=1
        if i<=j:
            swap(i,j)
            i+=1
            j-=1
    arr[s]=arr[j]
    arr[j]=pivot
    return j

n,k=map(int,input().split())
arr=list(map(int,input().split()))
quicksort(0,n-1,k-1)
print(arr[k-1])

# def mergesort(arr):
#     if len(arr)<2:
#         return arr
#     mid=len(arr)//2
#     low,high=mergesort(arr[:mid]),mergesort(arr[mid:])
#     merge=[]
#     l,h=0,0
#     while l<len(low) and h<len(high):
#         if low[l]<high[h]:
#             merge.append(low[l])
#             l+=1
#         else:
#             merge.append(high[h])
#             h+=1
#     merge+=low[l:]
#     merge+=high[h:]
#     return merge

# n,k=map(int,input().split())
# print(mergesort(list(map(int,input().split())))[k-1])

# def quicksort(arr):
#     if len(arr)<2:
#         return arr
#     pivot=arr[len(arr)//2]
#     left,mid,right=[],[],[]
#     for value in arr:
#         if value<pivot:
#             left.append(value)
#         elif value>pivot:
#             right.append(value)
#         else:
#             mid.append(value)
#     return quicksort(left)+mid+quicksort(right)

# n,k=map(int,input().split())
# arr=list(map(int,input().split()))
# arr=quicksort(arr)
# print(arr[k-1])