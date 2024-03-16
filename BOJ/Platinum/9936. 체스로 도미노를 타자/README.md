# BAEKJOON ONLINE JUDGE - 9936. 체스로 도미노를 타자

- [문제출처](https://www.acmicpc.net/problem/9936 '9936. 체스로 도미노를 타자')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 비트마스킹
- 비트필드를 이용한 다이나믹 프로그래밍

## 풀이

### 접근

- `DP` + 비트마스킹

### 점화식

```
if (status & 1)
    ret = cover(idx + 1, status >> 1, cnt);
else
{
    ret = cover(idx + 1, status >> 1, cnt);

    if (idx + 3 < n * 3)
        ret = max(ret, cover(idx + 1, status >> 1 | 4, cnt - 1) + chess[idx] + chess[idx + 3]);

    if (idx % 3 != 2 && !(status & 2))
        ret = max(ret, cover(idx + 2, status >> 2, cnt - 1) + chess[idx] + chess[idx + 1]);
}
```

### 설계

- `dp[i][j][k]`: `k`개만큼 도미노를 쌓을 수 있을 때 `i`번째 칸을 보고 있는 상태에서 `i`번째 칸부터 `i + 2`번째 칸까지 `3`개의 칸의 상태가 `j`일 때의 최댓값
  - `j`를 비트필드로 구현
  - `j`의 `3`번째 비트 값은 `i + 2`번재 칸이 채워져 있으면 1, 아니면 0으로 구현
- `cover(idx, status, cnt)`: `cnt`만큼 칸을 채울 수 있는 횟수로 `idx ~ idx + 2`번째 칸의 상태가 `status`이고 `idx`번째 칸을 채우려고 할 때의 최댓값
  - `2 x 1`크기와 `1 x 2`크기로 채우는 경우를 조건을 통해 판단 후 구현
- 파이썬으로 시간 초과, 메모리 초과가 발생하여 C++로 변환해서 제출
