# BAEKJOON ONLINE JUDGE - 16988. Baaaaaaaaaduk2 (Easy)

- [문제출처](https://www.acmicpc.net/problem/16988 '16988. Baaaaaaaaaduk2 (Easy)')

## 알고리즘 분류

- 그래프 이론
- 브루트포스
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색

## 풀이

### 접근

- `BFS`

### 설계

- 빈칸에 바둑돌 2개를 넣는 경우를 `combinations`로 구함
- 바둑돌을 두었을 때 죽일 수 있는 돌의 갯수를 BFS로 탐색 후 최댓값 갱신
