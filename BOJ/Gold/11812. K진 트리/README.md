# BAEKJOON ONLINE JUDGE - 11812. K진 트리

- [문제출처](https://www.acmicpc.net/problem/11812 '11812. K진 트리')

## 알고리즘 분류

- 수학
- 트리
- 최소 공통 조상상

## 풀이

### 접근

- 구현

### 설계

- 2번 이후의 노드를 0번부터 시작하도록 설계
- 현재 노드의 부모 노드는 `k`로 나눈 몫에 1을 더한 값과 같음 == `(x - 2 + k) // k`
- 두 노드가 같아질때까지 부모 노드를 찾아 올라가면서 높이를 구함
