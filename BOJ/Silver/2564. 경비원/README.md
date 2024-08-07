# BAEKJOON ONLINE JUDGE - 2564. 경비원
* [문제출처](https://www.acmicpc.net/problem/2564 "2564. 경비원")

## 알고리즘 분류
- 구현
- 많은 조건 분기

## 풀이
### 접근
- 동서남북 위치가 같은 경우와 다른 경우로 나눠서 조건분기 설정
- 동서남북 위치가 다른 경우 최솟값이 되는 경우 탐색

### 설계
- 모든 경우에 대해 조건을 통해 최솟값을 찾는다.
- 경비원과 상점의 동서남북 위치가 같은 경우 거리 차의 절댓값을 결과에 더해준다.
- 경비원과 상점의 동서남북 위치가 다른 경우
- 서로 반대 방향에 있는 경우(동서 or 남북) 최솟값은 시계방향이 될수도 반시계방향이 될수도 있기 때문에 두 경우의 최솟값을 구한다.
- 반대 방향이 아닌경우 경비원-상점의 방향이 시계방향인 경우에는 시계방향이 반시계방향인 경우에는 반시계방향이 최솟값이므로 그에 따른 거리를 구한다.
- (ex 남서=시계, 서북=시계, 서남=반시계, 북서=반시계)