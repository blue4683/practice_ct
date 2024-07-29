# BAEKJOON ONLINE JUDGE - 13144. List of Unique Numbers

- [문제출처](https://www.acmicpc.net/problem/13144 '13144. List of Unique Numbers')

## 알고리즘 분류

- 투 포인터

## 풀이

### 접근

- 구현

### 설계

- 투 포인터로 범위를 지정해 탐색
  - `end` 포인터가 이미 탐색한 숫자라면 그 전까지의 조합은 `end - start + 1`이므로 결과값에 더해줌
  - `end` 포인터가 `n - 1`이고, `start` 포인터가 `n - 1` 보다 작다면 `n - 1`이 될 때까지 증가시키면서 `end - start + 1`을 더해줌
