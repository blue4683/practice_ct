# BAEKJOON ONLINE JUDGE - 1913. 달팽이

* [문제출처](https://www.acmicpc.net/problem/1913 "1913. 달팽이")

## 알고리즘 분류

- 구현

## 풀이

### 설계

- `(dir+i)%4`를 통해 반시계 방향으로 경로 탐색
    - 진행 방향에 값이 있거나 범위 밖인 경우 반시계 방향으로 방향 변경
- `target`과 값이 같은 경우 좌표 저장