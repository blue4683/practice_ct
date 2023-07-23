# import sys
# input=sys.stdin.readline

# def remove(inven,taken,cnt):
#     return inven+cnt,taken+2*cnt

# def put(used,taken,cnt):
#     return used+cnt,taken+cnt

# n,m,b=map(int,input().split())
# blocks=[list(map(int,input().split())) for _ in range(n)]
# height=0
# answer=[256*m*n,0]

# while height<=256:
#     inven,taken,used=b,0,0
#     for y in range(n):
#          for x in range(m):
#              block=blocks[y][x]
#              if block>=height: inven,taken=remove(inven,taken,block-height)
#              else: used,taken=put(used,taken,height-block)
#     if used<=inven and taken<=answer[0]:
#         answer=[taken,height]
#     height+=1

# print(*answer)

import sys
input=sys.stdin.readline

n,m,b=map(int,input().split())
blocks=[0]*257
for _ in range(n):
    for i in map(int,input().split()): blocks[i]+=1
total=sum(i*blocks[i] for i in range(257))
answer=[total*2,0]
required=0
lower=blocks[0]
nm=n*m

for height in range(1,257):
    required+=lower
    total-=nm-lower
    if total+b<required: break
    else: answer=min([total*2+required,-height],answer)
    lower+=blocks[height]

print(answer[0],-answer[1])