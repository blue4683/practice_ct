from itertools import combinations
import sys
input=sys.stdin.readline

def find_combination(i):
    arr=list(map(sum,combinations(nums,i)))
    return sum(list(map(lambda x:int(x==s),arr)))

n,s=map(int,input().split())
nums=list(map(int,input().split()))
answer=0

for i in range(1,n+1):
    answer+=find_combination(i)

print(answer)