max_height=max_width=0
num = int(input())
directions = [list(map(int, input().split())) for _ in range(6)]
length = list(map(lambda x:x[1], directions))
idx = list(map(lambda x:x[0], directions))
idx *= 2
length *= 2
for direction in directions:
    max_height=direction[1] if direction[1]>max_height and direction[0]>=3 else max_height
    max_width=direction[1] if direction[1]>max_width and direction[0]<3 else max_width
for i in range(len(idx)):
    if idx[i:i+2]==idx[i+2:i+4]:
        small = length[i+1]*length[i+2]
        break
big = max_height*max_width
print((big-small)*num)