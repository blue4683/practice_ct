# BAEKJOON ONLINE JUDGE - 2295. 세 수의 합

- [문제출처](https://www.acmicpc.net/problem/2295 '2295. 세 수의 합')

## 알고리즘 분류

- 자료 구조
- 이분 탐색
- 해시를 사용한 집합과 맵
- 중간에서 만나기

## 풀이

### 접근

- 구현

### 설계

- 집합의 두 원소를 합한 값을 저장하는 집합 생성
  - 두 원소는 중복 가능
- 가장 큰 수부터 시작해 가장 큰 수에서 다른 집합의 원소를 뺐을 때 위에서 생성한 집합에 존재한다면 3개의 수의 합으로 만들 수 있는 수이므로 결과값을 출력
  - `k = x + y + z`를 변형해 `k - z = x + y` 임을 이용
