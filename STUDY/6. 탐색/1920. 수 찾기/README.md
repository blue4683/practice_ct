# BAEKJOON ONLINE JUDGE - 1920. 수 찾기

* [문제출처](https://www.acmicpc.net/problem/1920 "1920. 수 찾기")

## 알고리즘 분류
- 자료 구조
- 정렬
- 이분 탐색

## 풀이
### 접근
- `set` 활용

### 설계
- 중복된 수를 제거하기 위해 주어진 리스트를 `set`으로 변환
- 찾을 수들을 `set`을 돌면서 있으면 `1`을 없으면 `0`을 출력한다.