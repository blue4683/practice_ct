# BAEKJOON ONLINE JUDGE - 1940. 주몽

* [문제출처](https://www.acmicpc.net/problem/1940 "1940. 주몽")

## 알고리즘 분류
- 정렬
- 투 포인터

## 풀이
- 투 포인터로 접근
- 고유 번호 리스트를 정렬(투 포인터를 사용하기 위한 준비)
- start와 end의 값의 합이 m보다 크다면 end 인덱스를 1 감소
- 합이 m보다 작다면 start 인덱스를 1 증가
- 합이 m과 같다면 카운트를 1 올리고 start 인덱스를 1 증가
- start가 end보다 커지면 반복문 종료 후 카운트 출력