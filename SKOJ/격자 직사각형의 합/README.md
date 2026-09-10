# SKOJ - 격자 직사각형의 합

- [문제출처](https://skoj.site/problem/10300 '격자 직사각형의 합')

## 풀이

### 접근

- `2차원 누적합`

### 설계

- `(h+1) x (w+1)` 크기의 누적합 배열에서 `prefix[y][x] = prefix[y-1][x] + prefix[y][x-1] - prefix[y-1][x-1] + arr[y-1][x-1]`로 2차원 누적합 구성
- 질의 `(r1, c1, r2, c2)`마다 포함·배제 원리로 `prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]`를 계산해 O(1)에 구간 합 처리
