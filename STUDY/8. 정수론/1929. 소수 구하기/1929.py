m,n=map(int,input().split())
check = [1 for i in range(n+1)]
check[1]=0
i=2
while i<=n:
    j=2
    while i*j<=n:
        check[i*j]=0
        j+=1
    i+=1

for i in range(m,n+1):
    if check[i]:
        print(i)