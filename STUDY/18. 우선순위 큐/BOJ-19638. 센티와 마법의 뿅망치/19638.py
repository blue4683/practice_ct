from queue import PriorityQueue
import sys
input=sys.stdin.readline

n,h,t=map(int,input().split())
q=PriorityQueue()
for _ in range(n): q.put(-int(input()))
cnt=0

while cnt<=t:
    MAX=q.get()
    if MAX>-h or MAX==-1: break
    q.put(int(MAX/2))
    cnt+=1

if MAX>-h:
    print('YES')
    print(cnt)
else:
    print('NO')
    print(-MAX)