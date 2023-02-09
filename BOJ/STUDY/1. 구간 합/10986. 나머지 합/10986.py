import sys
input=sys.stdin.readline

n,m = map(int,input().split())
arr=list(map(int,input().split()))
acc_sum=[0]*n
acc_sum[0]=arr[0]
cnt=[0]*m
for i in range(1,n):
    acc_sum[i]+=arr[i]+acc_sum[i-1]
acc_sum=list(map(lambda x:x%m,acc_sum))
for value in acc_sum:
    cnt[value]+=1
result=cnt[0]
for i in range(m):
    if cnt[i]>1:
        result+=((cnt[i]*(cnt[i]-1))//2)
print(result)