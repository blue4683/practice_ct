from queue import PriorityQueue
import sys
input=sys.stdin.readline

n=int(input())
cards=PriorityQueue()
for _ in range(n):
    cards.put(int(input()))
result=0
while True:
    tmp=[]
    if cards.qsize()==1:
        break   
    a,b=cards.get(),cards.get()
    result+=a+b
    cards.put(a+b)
print(result)

# import sys
# input=sys.stdin.readline

# n=int(input())
# cards=sorted([int(input()) for _ in range(n)])
# result=0
# while len(cards)>1:
#     tmp=[]
#     if n%2:
#         tmp+=[cards.pop()]
#         n-=1
#     for i in range(0,n,2):
#         SUM=cards[i]+cards[i+1]
#         result+=SUM
#         tmp+=[SUM]
#     cards=sorted(tmp)
#     n=len(cards)
# print(result)