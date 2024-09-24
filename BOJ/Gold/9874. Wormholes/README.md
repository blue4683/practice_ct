# BAEKJOON ONLINE JUDGE - 9874. Wormholes

- [문제출처](https://www.acmicpc.net/problem/9874 '9874. Wormholes')

## 알고리즘 분류

- 그래프 이론
- 브루트포스
- 그래프 탐색
- 백트래킹

## 풀이

### 접근

- `DFS` + 백트래킹

### 설계

- `+x` 방향으로 이동해서 갈 수 있는 웜홀을 그래프로 표현
- 각각의 웜홀을 서로 겹치지 않게 `pair`로 연결
- 모든 `pair`가 있을 때 사이클이 존재하면 결과값에 `1`을 더해줌
