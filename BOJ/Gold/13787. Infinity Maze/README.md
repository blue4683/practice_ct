# BAEKJOON ONLINE JUDGE - 13787. Infinity Maze

- [문제출처](https://www.acmicpc.net/problem/13787 '13787. Infinity Maze')

## 알고리즘 분류

- 구현
- 시뮬레이션

## 풀이

### 접근

- 구현

### 설계

- 이동 횟수가 많으므로 `l`만큼 반복하지 않고 사이클을 찾아 위치를 유추
- 3차원 방문 배열을 만들어 `방향, y, x`를 인덱스로 최초로 도착했을 때의 이동횟수를 저장
  - 이동하면서 이전에 도착한 곳을 재방문할 경우 사이클이 생긴것으로 간주하고 계산
  - 사이클이 생기기 전에 이동이 끝나는 경우 마지막 위치와 방향 출력
