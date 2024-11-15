import sys
input = sys.stdin.readline


def travel_maze():
    money = cost[1]
    if money < 0:
        return 'No'

    visited = [0] * (n + 1)
    visited[1] = 1
    q = [(1, money)]
    while q:
        room, money = q.pop()
        for next_room in graph[room]:
            if visited[next_room]:
                continue

            if cost[next_room] < 0 and money + cost[next_room] < 0:
                continue

            if next_room == n:
                return 'Yes'

            if cost[next_room] > money:
                money = cost[next_room]

            elif cost[next_room] < 0:
                money += cost[next_room]

            visited[next_room] = 1
            q.append((next_room, money))

    return 'No'


while 1:
    n = int(input())
    if not n:
        break

    graph = [[] for _ in range(n + 1)]
    cost = [0] * (n + 1)
    for i in range(1, n + 1):
        s, *info = input().split()
        c, *rooms = map(int, info)
        if s == 'T':
            c *= - 1

        cost[i] = c
        for room in rooms[:-1]:
            graph[i].append(room)

    print(travel_maze())
