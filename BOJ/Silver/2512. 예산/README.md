# BAEKJOON ONLINE JUDGE - 2512. 예산

- [문제출처](https://www.acmicpc.net/problem/2512 '2512. 예산')

## 알고리즘 분류

- 이분 탐색
- 매개 변수 탐색

## 풀이

### 접근

- 구현

### 설계

- 최솟값을 `1`로 최댓값을 요청 금액의 최댓값으로 설정하고 그 둘의 중간값을 기준으로 이분탐색을 진행
  - 탐색시 매개 변수를 `요청 금액 - 중간값`으로 했을 때 남는 금액을 `중간값 * n`에서 빼서 최대 예산을 넘지 않으면 최솟값을 갱신하고 그렇지 않다면 최댓값을 갱신
