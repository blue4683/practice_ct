import sys
input = sys.stdin.readline

n, s, p = map(int, input().split())
if not n:
    print(1)
    sys.exit()

scores = list(map(int, input().split()))
rank = 1
same = 0

for i, score in enumerate(scores):
    if score > s:
        rank += 1

    if score == s:
        same = i + 1

print(rank) if same < p and rank <= p else print(-1)
