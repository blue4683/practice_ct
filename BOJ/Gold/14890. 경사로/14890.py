import sys
input = sys.stdin.readline


def find_road(arr):
    result = 0

    for y in range(n):
        height, cnt = arr[y][0], 1
        is_road = 1
        x = 1
        while x < n:
            if height == arr[y][x]:
                cnt += 1
                x += 1
                continue

            else:
                if height - arr[y][x] == 1:
                    if x + l <= n and arr[y][x:x + l].count(height - 1) == l:
                        x += l
                        height -= 1
                        cnt = 0
                        continue

                elif arr[y][x] - height == 1:
                    if cnt >= l:
                        height = arr[y][x]
                        cnt = 1
                        x += 1
                        continue

            is_road = 0
            break

        if is_road:
            result += 1

    return result


n, l = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n)]
rotate_roads = [[0] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        rotate_roads[y][x] = roads[x][y]

result = find_road(roads) + find_road(rotate_roads)
print(result)
