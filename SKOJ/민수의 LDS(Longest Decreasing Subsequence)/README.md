# SKOJ - 민수의 LDS(Longest Decreasing Subsequence)

- [문제출처](https://skoj.site/problem/10001 '민수의 LDS(Longest Decreasing Subsequence)')

## 풀이

### 접근

- `DP`

### 설계

- `dp[i]`를 `i`번째 원소로 끝나는 가장 긴 감소 부분수열의 길이로 정의
- `i`보다 앞선 인덱스 `j` 중 `arr[i] < arr[j]`를 만족하는 경우에 한해 `dp[j] + 1`로 갱신하는 O(N²) DP로 전체 최댓값 계산
