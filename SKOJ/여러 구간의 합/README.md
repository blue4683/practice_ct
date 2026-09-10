# SKOJ - 여러 구간의 합

- [문제출처](https://skoj.site/problem/10299 '여러 구간의 합')

## 풀이

### 접근

- `누적합`

### 설계

- 파이썬의 음수 인덱싱(`prefix[-1]`이 `prefix[n]`을 가리키는 성질)을 이용해 `i=0`일 때도 별도 예외 처리 없이 `prefix[i] = prefix[i-1] + arr[i]`로 누적합 구성
- 1-indexed 질의 `(l, r)`마다 `prefix[r-1] - prefix[l-2]`로 구간 합을 O(1)에 계산
