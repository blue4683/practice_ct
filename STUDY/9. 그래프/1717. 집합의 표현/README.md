# BAEKJOON ONLINE JUDGE - 1717. 집합의 표현

* [문제출처](https://www.acmicpc.net/problem/1717 "1717. 집합의 표현")

## 알고리즘 분류
- 자료 구조
- 분리 집합

## 풀이
### 설계
- 유니온 파인드
- `find`를 수행할 때마다 자신의 부모 노드를 저장(시간 초과 방지)
- `RecursionError`가 계속 떠서 `sys.setrecursionlimit(int(1e6))`로 해결(다른 방법이 있나...)