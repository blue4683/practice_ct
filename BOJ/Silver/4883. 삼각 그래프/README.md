# BAEKJOON ONLINE JUDGE - 4883. 삼각 그래프

- [문제출처](https://www.acmicpc.net/problem/1788 '4883. 삼각 그래프')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for y in range(n):
    for x in range(3):
        if (y, x) == (0, 1):
            continue

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue

            dp[y][x] = min(dp[y][x], dp[yy][xx] + graph[y][x])

```

### 설계

- 위에서부터 탐색하며 현재 노드로 이동할 수 있는 노드를 거쳤을 때 최소 비용을 배열에 저장
