import sys
input=sys.stdin.readline

result=[0]*101
result[1]=1
result[2]=1
result[3]=1
result[4]=2
result[5]=2

for i in range(6,101):
    result[i]=result[i-1]+result[i-5]

for _ in range(int(input())):
    print(result[int(input())])