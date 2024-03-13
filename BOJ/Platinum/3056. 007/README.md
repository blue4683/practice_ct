# BAEKJOON ONLINE JUDGE - 3056. 007

- [문제출처](https://www.acmicpc.net/problem/3056 '3056. 007')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 비트마스킹
- 비트필드를 이용한 다이나믹 프로그래밍

## 풀이

### 접근

- `DP` + 비트마스킹

### 점화식

```
for i in range(n):
    if status & (1 << i) == 0:
        dp[status] = max(dp[status], rates[now][i]
                            * mission(now + 1, status | (1 << i)) / 100)
```

### 설계

- `now`번째 요원에게 미션 할당 여부를 저장한 비트 `status`에서 할당된 미션을 제외한 미션을 할당했을 때 최대 확률 탐색
