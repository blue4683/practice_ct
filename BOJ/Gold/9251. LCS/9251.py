a,b=list(input()),list(input())
n,m=len(a),len(b)
lcs=[[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i==0 or j==0: lcs[i][j]=0
        elif a[i-1]==b[j-1]: lcs[i][j]=lcs[i-1][j-1]+1
        else: lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])

print(lcs[n][m])