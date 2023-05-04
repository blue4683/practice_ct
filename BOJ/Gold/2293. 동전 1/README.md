# BAEKJOON ONLINE JUDGE - 2293. 동전 1

- [문제출처](https://www.acmicpc.net/problem/2293 "2293. 동전 1")

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python
value[i]=value[i]+value[i-coin]
```

### 설계

- 작은 동전부터의 경우의 수를 구하면서 점화식 탐색
- 점화식 구현