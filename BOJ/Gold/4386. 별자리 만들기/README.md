# BAEKJOON ONLINE JUDGE - 4386. 별자리 만들기

- [문제출처](https://www.acmicpc.net/problem/4386 '4386. 별자리 만들기')

## 알고리즘 분류

- 그래프 이론
- 최소 스패닝 트리

## 풀이

### 설계

- 모든 별 사이들의 거리를 `edges`에 저장한다.
- 거리가 짧은 순으로 정렬 후 유니온 파인드를 거치면서 연결되어 있지 않다면 연결하고 결과값에 거리를 더해준다.
