a,b=sorted(map(int,input().split()))
r=0
while 1:
    if not b%a:
        r=a
        break
    r=b%a
    b=a
    a=r
print('1'*r)