import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr=sorted([list(map(int,input().split())) for _ in range(n)])
    pivot=arr[0][1]
    result=1
    for i in range(1,len(arr)):
        if arr[i][1]<pivot:
            result+=1
            pivot=arr[i][1]
    print(result)