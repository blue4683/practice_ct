# BAEKJOON ONLINE JUDGE - 1082. 방 번호

- [문제출처](https://www.acmicpc.net/problem/1082 '1082. 방 번호')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그리디 알고리즘

## 풀이

### 접근

- `DP`

### 점화식

```python

for k in range(m + 1):
    for i in range(n):
        if k < costs[i]:
            continue

        dp[k] = max(dp[k], make_num(dp[k - costs[i]], i))

```

### 설계

- 비용에 따라 만들 수 있는 수 중 가장 큰 수를 테이블에 저장하며 탐색
