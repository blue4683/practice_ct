string=input().split('-')
result=0
for i in range(len(string)):
    tmp=sum(list(map(int,string[i].split('+'))))
    if i==0:
        result+=tmp
    else:
        result-=tmp
print(result)

# import sys
# input=sys.stdin.readline

# def cal(a,o,b):
#     if o=='+':
#         return a+b
#     else:
#         return a-b
    
# def find(focus, value):
#     global result
#     if focus==n-1:
#         result=min(value,result)
#         return
#     find(focus+2, cal(value,num[focus+1],num[focus+2]))
#     if focus+4<n:
#         find(focus+4, cal(value, num[focus+1], cal(num[focus+2], num[focus+3], num[focus+4])))

# string=input().rstrip('\n')
# num=[]
# mid=0
# for i in range(len(string)):
#     try:
#         int(string[i])
#     except:
#         num+=[int(string[mid:i])]
#         num+=[string[i]]
#         mid=i+1
# num+=[int((string[mid:]))]
# n=len(num)
# result=1e9
# find(0,num[0])
# print(result)