# BAEKJOON ONLINE JUDGE - 14002. 가장 긴 증가하는 부분 수열 4

- [문제출처](https://www.acmicpc.net/problem/14002 '14002. 가장 긴 증가하는 부분 수열 4')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)


```

### 설계

- 현재 값이 이전 값보다 클 경우 `dp` 테이블 업데이트
- `dp` 테이블에서 가장 큰 값 출력
- `dp` 테이블을 역순으로 탐색하여 가장 큰 값 부터 시작해 `-1`을 하여 부분 수열 원소 탐색 후 리스트에 저장
- 리스트를 역순으로 정렬하여 출력
