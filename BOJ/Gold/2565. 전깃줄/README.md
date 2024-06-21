# BAEKJOON ONLINE JUDGE - 2565. 전깃줄

- [문제출처](https://www.acmicpc.net/problem/2565 '2565. 전깃줄')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(n):
    for j in range(i):
        if lines[i][1] >= lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

```

### 설계

- 주어진 전깃줄을 정렬
- 제거할 전깃줄을 저장하는 `dp` 테이블 생성
- 한 전깃줄의 `B`의 위치가 이전 전깃줄의 `B`의 위치보다 크다면 교차한다는 의미이므로 줄을 없앨지 말지 크기 비교후 `dp` 테이블 업데이트
- 모든 전깃줄을 비교 후 `n`에서 `dp` 테이블의 최댓값을 빼준 값 출력
