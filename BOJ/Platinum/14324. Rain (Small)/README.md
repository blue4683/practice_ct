# BAEKJOON ONLINE JUDGE - 14324. Rain (Small)

- [문제출처](https://www.acmicpc.net/problem/14324 '14324. Rain (Small)')

## 알고리즘 분류

- 구현
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색

## 풀이

### 접근

- `BFS`

### 설계

- 주어진 배열을 `0`으로 둘러싼 배열 생성
- 1부터 최대 높이까지 높여가면서 외곽에서 기준 높이 이하의 cell들을 탐색
  - 탐색이 끝났을 때 기준 높이보다 낮은 cell들이 존재하면 그 cell들의 높이를 기준 높이로 바꾸고 결과값에 `+1`을 해줌