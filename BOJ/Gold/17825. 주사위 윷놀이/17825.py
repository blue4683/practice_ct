import sys
input = sys.stdin.readline


class Node:
    def __init__(self, score, link, shortcut):
        self.score = score
        self.link = link
        self.shortcut = shortcut


def dfs(depth, pieces, score):
    global result
    if depth == 10:
        result = max(result, score)
        return

    for i in range(4):
        tmp = pieces[i]
        piece = pieces[i]
        for j in range(dices[depth]):
            if not j and plate[piece].shortcut:
                piece = plate[piece].shortcut

            else:
                piece = plate[piece].link

        if piece != 32 and piece in pieces:
            continue

        pieces[i] = piece
        dfs(depth + 1, pieces, score + plate[piece].score)
        pieces[i] = tmp


plate = [0] * 33
for i in range(21):
    plate[i] = Node(i << 1, i + 1, 0)

plate[32] = Node(0, 32, 0)
plate[5].shortcut = 21
plate[10].shortcut = 24
plate[15].shortcut = 26
plate[20].link = 32

plate[21] = Node(13, 22, 0)
plate[22] = Node(16, 23, 0)
plate[23] = Node(19, 29, 0)

plate[24] = Node(22, 25, 0)
plate[25] = Node(24, 29, 0)

plate[26] = Node(28, 27, 0)
plate[27] = Node(27, 28, 0)
plate[28] = Node(26, 29, 0)

for i in range(3):
    plate[29 + i] = Node(25 + (5 * i), 30 + i, 0)

plate[31].link = 20

dices = tuple(map(int, input().split()))
result = 0
dfs(0, [0] * 4, 0)

print(result)
