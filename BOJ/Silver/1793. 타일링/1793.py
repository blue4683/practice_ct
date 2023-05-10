import sys
inputs=sys.stdin.readlines()
MAX=251
dp=[0]*MAX
dp[0]=1
dp[1]=1
for i in range(2,MAX):
    dp[i]=dp[i-1]+2*dp[i-2]

for input in inputs:
    print(dp[int(input)])