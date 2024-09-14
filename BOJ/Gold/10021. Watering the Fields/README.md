# BAEKJOON ONLINE JUDGE - 10021. Watering the Fields

- [문제출처](https://www.acmicpc.net/problem/10021 '10021. Watering the Fields')

## 알고리즘 분류

- 그래프 이론
- 최소 스패닝 트리

## 풀이

### 접근

- 프림 알고리즘

### 설계

- 시작 노드부터 탐색 시작
- 힙에 `(넓이, 현재 노드)`를 넣은 뒤 넓이가 작은 순으로 탐색 진행
- 모든 노드에 대해 넓이를 구해 넓이가 `c` 이상일 경우 힙에 넣어서 탐색
- 탐색이 종료되었을 때 `connected`가 `1`로만 채워져 있다면 모두 연결되어 있는 것을 의미하므로 `result`를 반환하고 그렇지 않다면 `-1` 반환
