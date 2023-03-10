# def dfs(depth,num):
#     global result
#     if depth==n:
#         if not p[int(num)]:
#             result+=[int(num)]
#         return
#     for i in range(1,10):
#         tmp=num+str(i)
#         if not p[int(tmp)]: dfs(depth+1,tmp)

# n=int(input())
# max_n=int(10**(n+1))
# p=[0]*max_n
# p[1]=1
# i=2
# for i in range(2,int(max_n**0.5)+1):
#     if not p[i]:
#         for j in range(i*2,max_n,i):
#             p[j]=1
# result=[]
# dfs(0,'')
# result.sort()
# for res in result:
#     print(res)

def isprime(num):
    for i in range(2,num//2+1):
        if not num%i:
            return 0
    return 1

def dfs(num):
    if len(str(num))==n:
        print(num)
        return
    for i in range(1,10):
        if not i%2: continue
        if isprime(num*10+i): dfs(num*10+i)

n=int(input())
for i in [2,3,5,7]:
    dfs(i)