# BAEKJOON ONLINE JUDGE - 5052. 전화번호 목록

- [문제출처](https://www.acmicpc.net/problem/5052 '5052. 전화번호 목록')

## 알고리즘 분류

- 자료 구조
- 문자열
- 정렬
- 트리
- 트라이

## 풀이

### 접근

- 트라이

### 설계

- 트라이 구현 후 길이가 짧은 번호부터 `insert`
  - `insert` 하기 전 `search` 중간에 `is_end`인 문자열이 있다면 일관성이 없으므로 `NO` 출력
  - 모든 문자열을 `search` 후 `insert` 한다면 `YES` 출력
