import sys
input = sys.stdin.readline


class Room:
    def __init__(self, limit):
        self.limit = limit
        self.members = []


p, m = map(int, input().split())
rooms = []

for _ in range(p):
    l, n = input().split()
    l = int(l)

    for room in rooms:
        if len(room.members) == m:
            continue

        std_level = room.members[0][0]
        if std_level - 10 <= l <= std_level + 10:
            room.members.append((l, n))
            break

    else:
        room = Room(m)
        room.members.append((l, n))
        rooms.append(room)

for room in rooms:
    if len(room.members) == m:
        print('Started!')

    else:
        print('Waiting!')

    room.members.sort(key=lambda x: x[-1])
    for member in room.members:
        print(*member)
