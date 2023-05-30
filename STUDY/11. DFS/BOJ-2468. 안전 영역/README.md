# BAEKJOON ONLINE JUDGE - 2468. 안전 영역

* [문제출처](https://www.acmicpc.net/problem/2468 "2468. 안전 영역")

## 알고리즘 분류

- 그래프 이론
- 브루트포스 알고리즘
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색

## 풀이

### 설계

- `1 ~ MAX`까지의 경우 탐색
    - 탐색 방법은 `BFS, DFS` 둘 중 하나 택
        - 단 `DFS`의 경우 `recursionlimit`를 늘려줘야한다.
- 모든 경우 중 최대값 출력