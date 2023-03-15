# BAEKJOON ONLINE JUDGE - 13023. ABCDE

* [문제출처](https://www.acmicpc.net/problem/13023 "13023. ABCDE")

## 알고리즘 분류
- 그래프 이론
- 그래프 탐색
- 깊이 우선 탐색
- 백트래킹

## 풀이
### 접근
- DFS로 접근

### 설계
- 주어진 연결 요소를 통해 인접 그래프 정의
- DFS를 통해 재귀가 5번 일어나면 `result`를 1로 변환하고 반환
- 결과 출력