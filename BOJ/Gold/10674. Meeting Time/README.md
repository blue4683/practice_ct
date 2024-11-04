# BAEKJOON ONLINE JUDGE - 10674. Meeting Time

- [문제출처](https://www.acmicpc.net/problem/10674 '10674. Meeting Time')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론

## 풀이

### 접근

- `DP`

### 점화식

```python

visited[0][0] = 1
q = deque([(0, 1)])
while q:
    time, now = q.popleft()
    for field in graph[now]:
        next_time = time + field[index]
        if visited[field[0]][next_time]:
            continue

        visited[field[0]][next_time] = 1
        q.append((next_time, field[0]))

```

### 설계

- `field의 개수 * 최대 소요 시간`의 크기를 가진 2차원 배열을 2개 생성
- Bessie와 Elsie가 1번 필드에서 시작해서 n번 필드까지 가면서 걸리는 시간을 인덱스로 배열에 방문 체크
- 두 배열의 `n`번째 배열을 순회하며 동시에 도착하는 가장 작은 시간을 찾아 출력
