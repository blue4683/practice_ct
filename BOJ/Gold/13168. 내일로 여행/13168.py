import sys
input = sys.stdin.readline
INF = float('inf')
fee_rate = {'Subway': 1, 'Bus': 1, 'Taxi': 1, 'Airplane': 1, 'KTX': 1, 'S-Train': 0.5,
            'V-Train': 0.5, 'ITX-Saemaeul': 0, 'ITX-Cheongchun': 0, 'Mugunghwa': 0}


def floyd(dist):
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if dist[start][end] > dist[start][mid] + dist[mid][end]:
                    dist[start][end] = dist[start][mid] + dist[mid][end]

    return dist


n, r = map(int, input().split())
cities = set(input().split())
city_num = {city: num for num, city in enumerate(cities)}

m = int(input())
dests = list(map(lambda x: city_num[x], input().split()))

ticket = [[INF] * n for _ in range(n)]
no_ticket = [[INF] * n for _ in range(n)]
for i in range(n):
    ticket[i][i] = 0
    no_ticket[i][i] = 0

for _ in range(int(input())):
    trans, a, b, cost = input().split()
    y, x = map(lambda x: city_num[x], [a, b])
    ticket[y][x] = min(ticket[y][x], float(cost) * fee_rate[trans])
    ticket[x][y] = min(ticket[x][y], float(cost) * fee_rate[trans])
    no_ticket[y][x] = min(no_ticket[y][x], float(cost))
    no_ticket[x][y] = min(no_ticket[x][y], float(cost))

ticket, no_ticket = map(floyd, [ticket, no_ticket])
used, not_used = r, 0
for i in range(1, m):
    a, b = dests[i - 1], dests[i]
    used += ticket[a][b]
    not_used += no_ticket[a][b]

print('Yes') if used < not_used else print('No')
