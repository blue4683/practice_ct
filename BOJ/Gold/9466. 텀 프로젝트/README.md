# BAEKJOON ONLINE JUDGE - 9466. 텀 프로젝트

- [문제출처](https://www.acmicpc.net/problem/9466 '9466. 텀 프로젝트')

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 깊이 우선 탐색

## 풀이

### 접근

- `DFS`

### 설계

- 방문 배열에 체크하면서 탐색
- 방문한 적이 있는 번호일 때 현재 팀에 존재하면 방문한 번호의 인덱스부터 `result`에 저장
  - 중간부터 팀이 될 수 있는 경우가 있으므로 조심할 것
- 결과 출력
