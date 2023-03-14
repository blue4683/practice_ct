import sys
input = sys.stdin.readline

n=int(input())
arr=[[int(input()),i] for i in range(n)]
sorted_arr=sorted(arr)
dif=list(map(lambda x,y:y[1]-x[1],arr,sorted_arr))
max_dif=0
for d in dif:
    if d>max_dif:
        max_dif=d
print(max_dif+1)

# 1차
# def find(arr,cnt):
#     if sorted(arr)==arr:
#         return cnt
#     pivot=arr[cnt-1]
#     left,mid,right=[],[],[]
#     for value in arr:
#         if value<pivot:
#             left.append(value)
#         elif value>pivot:
#             right.append(value)
#         else:
#             mid.append(value)
#     if sorted(left)==left and sorted(right)==right:
#         return cnt+1
#     return find(left+mid+right,cnt+1)

# n=int(input())
# arr=[int(input()) for _ in range(n)]
# result=find(arr,1)
# print(result)