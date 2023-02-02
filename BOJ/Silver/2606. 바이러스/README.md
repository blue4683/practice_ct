# BAEKJOON ONLINE JUDGE - 2606. 바이러스

* [문제출처](https://www.acmicpc.net/problem/2606 "2606. 바이러스")

## 알고리즘 분류
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색

## 풀이
- 딕셔너리에 리스트를 저장하여 그래프를 구현하였다.
- 입력받은 쌍 서로를 `key`, `value`로 하여 딕셔너리에 저장한다.
```python
dict[key].append(value)
dict[value].append(key)
```
- 덱을 사용한 BFS 탐색을 진행한다.
- 이미 탐색한 적이 있는 컴퓨터는 탐색하지 않는다.
- 탐색 리스트의 합에서 1번 컴퓨터를 제외하기 위해 1을 뺀 값을 출력한다.

## 참고
- 그래프를 중첩 리스트를 사용하여 구현하는 방법을 찾아서 코드로 옮겨보았다.
```python
n=int(input())
v=int(input())
graph = [[] for i in range(n+1)]
for i in range(v):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
```