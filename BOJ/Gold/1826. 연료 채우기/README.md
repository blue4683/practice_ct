# BAEKJOON ONLINE JUDGE - 1826. 연료 채우기

- [문제출처](https://www.acmicpc.net/problem/1826 '1826. 연료 채우기')

## 알고리즘 분류

- 자료 구조
- 그리디 알고리즘
- 정렬
- 우선순위 큐

## 풀이

### 접근

- 구현

### 설계

- 주어진 주유소의 정보를 위치에 따라 정렬
- 가장 가가운 주유소부터 현재 위치에서 갈 수 있는지 없는지 판단
  - 갈 수 없는 경우 갈 수 있을때까지 최대 힙에서 연료를 꺼내서 사용하고 결과값 갱신
  - 연료를 다 쓴 상태에서도 갈 수 없는 경우 `-1` 출력
- 최대 힙에 방문한 주유소의 연료 양을 추가
