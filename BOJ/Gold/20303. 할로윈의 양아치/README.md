# BAEKJOON ONLINE JUDGE - 20303. 할로윈의 양아치

- [문제출처](https://www.acmicpc.net/problem/20303 '20303. 할로윈의 양아치')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 자료 구조
- 그래프 이론
- 그래프 탐색
- 분리 집합
- 배낭 문제

## 풀이

### 접근

- `유니온 파인드` + `DP`

### 점화식

```python

dp = [0] * (k)
for cnt, candy in candies:
    for j in range(k - 1, -1, -1):
        if not j and cnt < k:
            dp[cnt] = max(dp[cnt], candy)

        elif j and dp[j]:
            if j + cnt < k:
                dp[j + cnt] = max(dp[j + cnt], dp[j] + candy)

```

### 설계

- 유니온 파인드로 그래프를 연결하고 연결된 아이들의 수와 그 아이들의 사탕의 합을 배열에 저장
- dp배열의 길이를 `k`로 설정하고 `x` 명의 아이를 선택했을 때의 최대 사탕 개수를 `dp[x]`에 저장하고 최댓값 출력
