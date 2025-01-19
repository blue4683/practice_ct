# BAEKJOON ONLINE JUDGE - 10942. 팰린드롬?

- [문제출처](https://www.acmicpc.net/problem/10942 '10942. 팰린드롬?')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def find(s, e):
    if dp[s][e] != -1:
        return dp[s][e]

    if arr[s] != arr[e]:
        dp[s][e] = 0
        return 0

    if dp[s + 1][e - 1] == -1:
        dp[s + 1][e - 1] = find(s + 1, e - 1)
        dp[s][e] = dp[s + 1][e - 1]

    return dp[s + 1][e - 1]

```

### 설계

- 범위를 좁혀가며 팰린드롬인지 판단 후 2차원 배열에 저장
