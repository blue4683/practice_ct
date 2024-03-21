# BAEKJOON ONLINE JUDGE - 3176. 도로 네트워크

- [문제출처](https://www.acmicpc.net/problem/3176 '3176. 도로 네트워크')

## 알고리즘 분류

- 자료 구조
- 트리
- 최소 공통 조상
- 희소 배열

## 풀이

### 접근

- `LCA`

### 설계

- `x, y` 두 정점의 최단, 최장거리는 최소 공통 조상 `z`를 기준으로 `x ~ z`까지의 최단, 최장거리와 `y ~ z`까지의 최단, 최장거리를 비교한 것과 같음
- `LCA` 알고리즘에서 각 노드의 `2 ** n`번째 조상 노드까지의 노드와 최단, 최장거리를 `parents, short_distance, long_distance` 배열에 각각 저장
