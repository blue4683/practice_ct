# BAEKJOON ONLINE JUDGE - 13625. Boss

- [문제출처](https://www.acmicpc.net/problem/13625 '13625. Boss')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색

## 풀이

### 접근

- `DFS`

### 설계

- 그래프를 생성하여 본인의 직속 상관을 저장
- 생성한 그래프를 활용하여 직속 및 간접적으로 상관인 사람들의 번호를 저장하는 배열 생성하고 DFS로 탐색 후 저장
- 모든 사람들의 위치를 저장하는 배열과 위치에 존재하는 번호를 저장하는 배열을 생성하고, `T` 커맨드를 입력받았을때 갱신
- `P` 커맨드를 입력받으면 번호에 해당하는 위치에 존재하는 사람의 번호를 찾아 직속 및 간접적으로 상관인 사람들의 나이들을 비교하여 최솟값 출력
