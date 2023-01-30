import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
answer = 256*n*m
for height in range(257):
    make_blocks, required_blocks = 0, 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] >= height:
                make_blocks += ground[i][j] - height
            else:
                required_blocks += height - ground[i][j]
    if make_blocks+b >= required_blocks:
        if required_blocks + (make_blocks*2) <= answer:
            answer = required_blocks + (make_blocks*2)
            target = height
print(answer, target)