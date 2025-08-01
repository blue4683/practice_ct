# BAEKJOON ONLINE JUDGE - 1796. 신기한 키보드

- [문제출처](https://www.acmicpc.net/problem/1796 '1796. 신기한 키보드')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

def dfs(alp, pos):
    if alp == 26:
        return 0

    result = dp[pos][alp]
    if result != -1:
        return result

    result = 10 ** 9
    pl, pr = pos_l[alp], pos_r[alp]
    if exist[alp]:
        for i in range(n):
            result = min(result, dfs(alp + 1, i) +
                         min(get_dist(pos, i, pl, pr), get_dist(pos, i, pr, pl)))

    else:
        result = dfs(alp + 1, pos)

    dp[pos][alp] = result
    return dp[pos][alp]

```

### 설계

- 알파벳마다 가장 왼쪽에 있는 위치와 가장 오른쪽에 있는 위치를 구한 뒤 어느 곳을 먼저 방문했을 때 최솟값이 되는지를 탐색
