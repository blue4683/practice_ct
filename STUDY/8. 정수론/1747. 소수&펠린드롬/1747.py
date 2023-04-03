def check(s):
    length=len(s)
    for i in range(length//2):
        if s[i]!=s[length-i-1]: return False
    return True

n=int(input())
arr=[0]*(int(1e6)+5001)
target=[]
for i in range(2,int(1e6)+5001):
    if arr[i]: continue
    target+=[i]
    j=2
    while i*j<=int(1e6)+5000:
        arr[i*j]=1
        j+=1
for t in target:
    if t<n: continue
    flag=1
    str_num=str(t)
    if check(str_num):
        print(str_num)
        break