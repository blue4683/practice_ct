# BAEKJOON ONLINE JUDGE - 5022. 연결

- [문제출처](https://www.acmicpc.net/problem/5022 '5022. 연결')

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색

## 풀이

### 접근

- `BFS`

### 설계

- A를 먼저 최소 길이로 연결한 다음 B를 최소 길이로 연결하는 경우와 반대로 하는 경우를 BFS로 탐색
- 두 결과를 비교해 결과 출력
