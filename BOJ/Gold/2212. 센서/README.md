# BAEKJOON ONLINE JUDGE - 2212. 센서

- [문제출처](https://www.acmicpc.net/problem/2212 '2212. 센서')

## 알고리즘 분류

- 그리디 알고리즘
- 정렬

## 풀이

### 접근

- 정렬

### 설계

- 센서 정렬 후 센서 사이의 거리를 구해 리스트에 저장
- 거리 리스트를 정렬 후 가장 큰 거리부터 `k - 1`개만큼 `0`으로 만들고 나머지 거리의 합을 구함
  - 가장 큰 거리들을 `0`으로 만드는 것은 영역이 `0`인 집중국을 그 위치에 설치한 것과 같음
