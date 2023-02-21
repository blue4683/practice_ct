import sys
input = sys.stdin.readline

w,h=map(int,input().split())
n=int(input())
shops=[list(map(int,input().split())) for _ in range(n+1)]
result=0
dir,pos=shops.pop()
for shop in shops:
    d,p=shop
    if dir==d:
        result+=abs(pos-p)
    else:
        if (dir,d)==(1,2) or (dir,d)==(2,1):
            result+=min(pos+p+h,2*w-pos-p+h)
        elif (dir,d)==(1,3) or (dir,d)==(3,1):
            result+=pos+p
        elif (dir,d)==(1,4):
            result+=w-pos+p
        elif (dir,d)==(4,1):
            result+=w-p+pos
        elif (dir,d)==(2,3):
            result+=pos+h-p
        elif (dir,d)==(3,2):
            result+=p+h-pos
        elif (dir,d)==(2,4) or (dir,d)==(4,2):
            result+=w-pos+h-p
        elif (dir,d)==(3,4) or (dir,d)==(4,3):
            result+=min(pos+p+w,2*h-pos-p+w)
print(result)