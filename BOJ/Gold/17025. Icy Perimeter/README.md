# BAEKJOON ONLINE JUDGE - 17025. Icy Perimeter

- [문제출처](https://www.acmicpc.net/problem/17025 '17025. Icy Perimeter')

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색

## 풀이

### 접근

- `BFS`

### 설계

- 둘레를 측정하기 위해 주어진 배열을 `.`으로 둘러쌈
- `BFS`로 탐색하며 넓이와 둘레를 측정
  - 넓이는 `#`의 개수, 둘레는 방문하지 않은 `#`에서 `.`으로 가는 횟수(중복 가능)
