# BAEKJOON ONLINE JUDGE - 9461. 파도반 수열
* [문제출처](https://www.acmicpc.net/problem/9461 "9461. 파도반 수열")

## 알고리즘 분류

- 수학
- 다이나믹 프로그래밍

## 풀이

### 설계

- `i`가 6이상일때 다음과 같은 점화식을 만족
- `result[i]=result[i-1]+result[i-5]`