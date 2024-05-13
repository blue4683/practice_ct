# BAEKJOON ONLINE JUDGE - 1727. 커플 만들기

- [문제출처](https://www.acmicpc.net/problem/1727 '1727. 커플 만들기')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그리디 알고리즘
- 정렬

## 풀이

### 접근

- 정렬 + `DP`

### 점화식

```python

if i == j:
    dp[i][j] = dp[i - 1][j - 1] + abs(men[i - 1] - women[j - 1])

elif i > j:
    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] +
                    abs(men[i - 1] - women[j - 1]))

else:
    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1] +
                    abs(men[i - 1] - women[j - 1]))

```

### 설계

- 배열 정렬
- 인덱스가 같으면 무조건 커플, 다르면 여자 또는 남자가 솔로로 남을 수도 있으므로 이를 반영하여 `dp` 테이블 업데이트
