# BAEKJOON ONLINE JUDGE - 1941. 소문난 칠공주

* [문제출처](https://www.acmicpc.net/problem/1941 "1941. 소문난 칠공주")

## 알고리즘 분류

- 수학
- 그래프 이론
- 브루트포스 알고리즘
- 그래프 탐색
- 너비 우선 탐색
- 조합론
- 깊이 우선 탐색
- 백트래킹

## 풀이

### 설계

- 주어진 2차원 배열을 이어붙인 1차원 배열을 생성한다.
- `DFS`로 1차원 배열에서 7개를 선택하는 경우를 찾는다.
    - 백트래킹으로 `Y`가 4개이상 들어가는 경우는 제외한다.
    - 1차원 배열에서 선택한 인덱스 `i`를 `(i//5, i%5)`로 바꾸어 원래 2차원 배열의 인덱스를 저장하면서 진행한다.
- 조건에 맞게 7개를 선택하면 `BFS`를 통해 연결되어 있는지 확인한다.
    - 모두 연결되어 있다면 `result` 값을 1 증가시킨다.
- 결과를 출력한다.