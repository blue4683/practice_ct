# BAEKJOON ONLINE JUDGE - 1450. 냅색문제

- [문제출처](https://www.acmicpc.net/problem/1450 '1450. 냅색문제')

## 알고리즘 분류

- 이분 탐색
- 중간에서 만나기

## 풀이

### 접근

- 중간에서 만나기

### 설계

- 배열을 반으로 나눠 부분 수열을 각각 리스트에 저장
- 리스트 하나를 정렬한 뒤 정렬하지 않은 리스트를 기준으로 이분탐색으로 `c`를 넘지 않는 무게 조합의 개수를 `result`에 더해줌
