import sys
input = sys.stdin.readline

n,m=map(int,input().split())
num_list = list(map(int,input().split()))
sum_list = [0]+num_list+[0]
for idx in range(1,len(num_list)+1):
    sum_list[idx]+=sum_list[idx-1]
for _ in range(m):
    i,j=map(int,input().split())
    print(sum_list[j]-sum_list[i-1])