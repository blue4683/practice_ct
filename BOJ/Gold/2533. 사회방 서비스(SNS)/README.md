# BAEKJOON ONLINE JUDGE - 2533. 사회방 서비스(SNS)

- [문제출처](https://www.acmicpc.net/problem/2533 '2533. 사회방 서비스(SNS)')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 트리
- 트리에서의 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python
dp[now][1] += dp[next][0]
dp[now][0] += min(dp[next][1], dp[next][0])
```

### 설계

- 현재 노드가 얼리 어답터일 경우와 일반인일 경우에 해당하는 경우 계산
- 이전에 방문한 노드는 재탐색 X
