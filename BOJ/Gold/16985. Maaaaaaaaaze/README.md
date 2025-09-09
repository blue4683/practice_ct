# BAEKJOON ONLINE JUDGE - 16985. Maaaaaaaaaze

- [문제출처](https://www.acmicpc.net/problem/16985 '16985. Maaaaaaaaaze')

## 알고리즘 분류

- 구현
- 그래프 이론
- 브루트포스
- 그래프 탐색
- 너비 우선 탐색

## 풀이

### 접근

- `BFS`

### 설계

- 5개의 판을 각각 회전시키는 경우를 `product`로 구하고, 5개의 판을 쌓는 경우를 `permutation`으로 구함
- 위의 경우를 조합해 미로 배열을 생성하고 BFS 탐색 수행
