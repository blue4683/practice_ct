import sys
input=sys.stdin.readline
MIN,MAX=1e10,-1e10

def calculate(depth,num):
    global plus,minus,multiple,divide,MIN,MAX
    if depth==n:
        MIN,MAX=min(MIN,num),max(MAX,num)
        return
    
    if plus:
        plus-=1
        calculate(depth+1,num+nums[depth])
        plus+=1

    if minus:
        minus-=1
        calculate(depth+1,num-nums[depth])
        minus+=1

    if multiple:
        multiple-=1
        calculate(depth+1,num*nums[depth])
        multiple+=1

    if divide:
        divide-=1
        if num<0: calculate(depth+1,-(-num//nums[depth]))
        else: calculate(depth+1,num//nums[depth])
        divide+=1

n=int(input())
nums=list(map(int,input().split()))
plus,minus,multiple,divide=map(int,input().split())
calculate(1,nums[0])

print(MAX)
print(MIN)