# BAEKJOON ONLINE JUDGE - 2253. 점프

- [문제출처](https://www.acmicpc.net/problem/2253 '2253. 점프')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def dfs(now, before):
    if now == n:
        return 0

    if now > n or now in little:
        return INF

    result = dp[now][before]
    if result != -1:
        return result

    result = INF
    if before - 1 > 0:
        result = min(result, 1 + dfs(now + before - 1, before - 1))

    if before > 0:
        result = min(result, 1 + dfs(now + before, before))

    if before + 1 > 0:
        result = min(result, 1 + dfs(now + before + 1, before + 1))

    dp[now][before] = result
    return dp[now][before]

```

### 설계

- 현재 위치에서 이전 위치에서 점프한 칸수를 기준으로 몇칸 점프를 할 것인지를 재귀를 통해 탐색
