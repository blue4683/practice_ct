from collections import deque
import sys
input = sys.stdin.readline

computers = [0]*(int(input())+1)

d = {}
for _ in range(int(input())):
	a,b = map(int, input().split())
	try:
		d[a].append(b)
	except:
		d[a] = [b]
	try:
		d[b].append(a)
	except:
		d[b] = [a]

computers[1] = 1
q = deque([1])
while q:
	virus = q.popleft()
	try:
		com = d[virus]
	except:
		continue
	for c in com:
		if not computers[c]:
			computers[c] = 1
			q.append(c)
print(sum(computers)-1)