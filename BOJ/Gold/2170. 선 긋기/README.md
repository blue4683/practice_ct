# BAEKJOON ONLINE JUDGE - 2170. 선 긋기

- [문제출처](https://www.acmicpc.net/problem/2170 '2170. 선 긋기')

## 알고리즘 분류

- 정렬
- 스위핑

## 풀이

### 설계

- 선의 `x` 좌표를 오름차순으로 정렬
- 맨 처음의 선을 기준으로 선이 겹치는지 비교 후 `left, right` 업데이트
  - 겹치지 않는다면 결과값에 `right - left`를 더하고, `left, right`를 새롭게 정의
