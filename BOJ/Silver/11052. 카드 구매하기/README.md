# BAEKJOON ONLINE JUDGE - 11052. 카드 구매하기

- [문제출처](https://www.acmicpc.net/problem/11052 '11052. 카드 구매하기')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 설계

- `result[j] = max(result[j], result[j - i - 1] + price)`
