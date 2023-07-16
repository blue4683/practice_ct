# BAEKJOON ONLINE JUDGE - 12904. A와 B

* [문제출처](https://www.acmicpc.net/problem/12904 "12904. A와 B")

## 알고리즘 분류

- 구현
- 문자열
- 그리디 알고리즘

## 풀이

### 설계

- `DFS`로 목표 문자열의 두 가지 경우를 탐색
    - 문자열의 끝이 B인 경우 B를 제거하고 뒤집는다.
    - 아니라면 A를 제거한다.