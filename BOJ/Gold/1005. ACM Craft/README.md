# BAEKJOON ONLINE JUDGE - 1005. ACM Craft

* [문제출처](https://www.acmicpc.net/problem/1005 "1005. ACM Craft")

## 알고리즘 분류
- 다이나믹 프로그래밍
- 그래프 이론
- 위상 정렬

## 풀이

### 접근
- 위상 정렬

### 설계
- 선행조건이 없는 번호를 큐에 저장
- 큐에서 하나씩 `pop`하면서 본인을 선행조건으로 하는 원소의 `indegree` 값을 1 감소
- 결과 리스트에 이전 건설이 끝나는 시간의 최댓값을 저장 `(선행조건이 완료되어야 건설이 가능하기 때문에 가장 늦게 끝나는 시간을 저장)`
- `indegree`값이 `0`이면 큐에 추가
- 목표의 선행조건이 없을 경우`(indegree[w]=0)` 종료 후 결과 출력