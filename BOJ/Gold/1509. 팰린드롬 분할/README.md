# BAEKJOON ONLINE JUDGE - 1509. 팰린드롬 분할

- [문제출처](https://www.acmicpc.net/problem/1509 '1509. 팰린드롬 분할')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for end in range(n):
    for start in range(end + 1):
        if palindrome[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)

```

### 설계

- 2차원 배열을 만들어 `string[start : end + 1]`가 팰린드롬인지를 `palindrome[start][end]`에 저장
- `dp` 생성 후 `end`까지 최소 팰린드롬 분할 수를 찾아 업데이트
