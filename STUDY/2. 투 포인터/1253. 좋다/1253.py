import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().split())))
good = 0
for i in range(n):
    target = arr[i]
    start=0
    end=n-1
    while start<end:
        if arr[start]+arr[end]==target:
            if start!=i and end!=i:
                good+=1
                break
            elif start==i:
                start+=1
            else:
                end-=1
        elif arr[start]+arr[end]<target:
            start+=1
        else:
            end-=1
print(good)

# n = int(input())
# arr = sorted(list(map(int,input().split())))
# visited=[0]*n
# end=2
# good=0
# while end<n:
#     for s in range(end):
#         tmp=good
#         idx=s+1
#         while idx<end:
#             value = arr[s]+arr[idx]
#             if value==arr[end] and not visited[end]:
#                 visited[end]=1
#                 good+=1
#                 idx=end
#                 break
#             else:
#                 idx+=1
#         if tmp!=good:
#             break
#     end+=1
# print(good)