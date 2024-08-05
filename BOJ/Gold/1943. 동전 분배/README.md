# BAEKJOON ONLINE JUDGE - 1943. 동전 분배

- [문제출처](https://www.acmicpc.net/problem/1943 '1943. 동전 분배')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 배낭 문제

## 풀이

### 접근

- `DP`

### 점화식

```python
dp = [0] * 100001
dp[0] = 1
for i in range(n):
    value, cnt = coins[i]
    for v in range(half + 1, 0, -1):
        if dp[v - value]:
            for j in range(cnt):
                if v + j * value > half:
                    break

                dp[v + j * value] = 1
```

### 설계

- 동전의 총합이 절반으로 나눠지지 않으면 `0` 출력
- 동전의 금액마다 동전의 총합의 절반부터 `1`까지 탐색하며 `dp[v - value(동전의 금액)]`가 `1`인 곳이 있다면 동전의 개수로 만들 수 있는 금액을 더한 곳에 `1` 업데이트
- 동전의 총합의 절반인 곳이 `1`이라면 `1` 출력, 아니라면 `0` 출력
