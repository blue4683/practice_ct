n=int(input())
result=n
for i in range(2,int(n**0.5)+1):
    if not n%i:
        result-=result//i
        while not n%i:
            n//=i
if n>1:
    result-=result//n
print(result)