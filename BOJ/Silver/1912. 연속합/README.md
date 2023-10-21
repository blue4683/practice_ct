# BAEKJOON ONLINE JUDGE - 1912. 연속합
* [문제출처](https://www.acmicpc.net/problem/1912 "1912. 연속합")

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 설계

- `i`번째 누적합의 최댓값은 `i-1`번째 누적합을 더한 것과 아닌 것의 최댓값이다.
- `result[i]=max(result[i],result[i-1]+arr[i])`