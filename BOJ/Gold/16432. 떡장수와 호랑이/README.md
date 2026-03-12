# BAEKJOON ONLINE JUDGE - 16432. 떡장수와 호랑이

- [문제출처](https://www.acmicpc.net/problem/16432 '16432. 떡장수와 호랑이')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 그래프 탐색
- 깊이 우선 탐색

## 풀이

### 접근

- `DP`

### 점화식

```python

for item in arr[1]:
    dp[1][item] = 1

for day in range(2, n + 1):
    for item in arr[day]:
        for k in range(1, 10):
            if k != item and dp[day - 1][k]:
                dp[day][item] = 1
                prev[day][item] = k
                break

```

### 설계

- 그 날에 줄 수 있는 떡을 dp 배열에 저장
- prev 배열에 이전 날에 준 떡을 저장해 마지막에 경로를 역추적할 때 사용
