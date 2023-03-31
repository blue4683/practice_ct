MAX=int(1e7)+1
a,b=map(int,input().split())
r=0
arr=[0]*MAX
for i in range(2,int(b**0.5)+1):
    if arr[i]: continue
    for j in range(i*2,MAX,i):
        arr[j]=1
for i in range(2,int(b**0.5)+1):
    if not arr[i]:
        j=i
        while i*j<=b:
            i*=j
            if a<=i<=b:
                r+=1
print(r)