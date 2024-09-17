# BAEKJOON ONLINE JUDGE - 16639. 괄호 추가하기 3

- [문제출처](https://www.acmicpc.net/problem/16639 '16639. 괄호 추가하기 3')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 브루트포스

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(n + 1):
    for j in range(n - i + 1):
        k = i + j
        if k == j:
            dp[j][k].min = numbers[j]
            dp[j][k].max = numbers[j]

        else:
            dp[j][k].min, dp[j][k].max = calculate(j, k)

```

### 설계

- 범위 안에 있는 값들을 계산해 최솟값과 최댓값을 테이블에 저장
  - 최솟값의 경우 음수끼리 곱할 경우 최대가 될 수 있기 때문에 저장
