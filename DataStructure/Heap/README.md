# 힙(Heap)
## 힙이란?
- 완전 이진 트리의 일종으로 데이터에서 최댓값과 최솟값을 빠르게 찾기 위해서 만들어졌다.
- 위에서부터 밑으로 탐색하고, 왼쪽부터 오른쪽으로 탐색한다.
- (부모 노드의 인덱스) = (자식 노드의 인덱스)//2
- (왼쪽 자식 노드의 인덱스) = (부모 노드의 인덱스)*2
- (오른쪽 자식 노드의 인덱스) = (부모 노드의 인덱스)*2+1
- 우선순위 큐를 가장 효율적으로 구현할 수 있다.

</br>
<table class='table-fill' style='align:center'>
    <thead>
        <tr align='center'>
            <th class='text-center'>우선순위 큐를 구현하는 표현 방법</th>
            <th class='text-center'>삽입</th>
            <th class='text-center'>삭제</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class='text-center'>순서 없는 배열</td>
            <td class='text-center'><code>O(1)</code></td>
            <td class='text-center'><code>O(n)</code></td>
        </tr>
        <tr>
            <td class='text-center'>순서 없는 연결 리스트</td>
            <td class='text-center'><code>O(1)</code></td>
            <td class='text-center'><code>O(n)</code></td>
        </tr>
        <tr>
            <td class='text-center'>정렬된 배열</td>
            <td class='text-center'><code>O(n)</code></td>
            <td class='text-center'><code>O(1)</code></td>
        </tr>
        <tr>
            <td class='text-center'>정렬된 연결 리스트</td>
            <td class='text-center'><code>O(n)</code></td>
            <td class='text-center'><code>O(1)</code></td>
        </tr>
        <tr>
            <td class='text-center' style='background:#4E5066;color:#FFFFFF'>힙(heap)</td>
            <td class='text-center' style='background:#4E5066;color:#FFFFFF''><code>O(logn)</code></td>
            <td class='text-center' style='background:#4E5066;color:#FFFFFF''><code>O(logn)</code></td>
        </tr>
    </tbody>
</table>

</br>
<figure>
    <p align="center"><img src=../../img/heap.png width=50% title="SW Expert Academy"></p>
    <figcaption align='center'><a href="https://ko.wikipedia.org/wiki/%ED%9E%99_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0)" target='blank'>최대 힙 구조</a></figcaption>
</figure>

## 힙의 기능
- 예시 최대 힙
### 1. 삽입
- 힙은 완전 이진 트리이기때문에 기본적으로 왼쪽 하단부 노드부터 저장된다.
- 저장하고 힙은 부모 노드와 비교를 하는데 자신이 부모 노드보다 크다면 부모노드와 자리를 교환하게 된다. 이 동작은 자신이 부모 노드보다 작아질때까지 반복한다.
- 여기서는 값이 100 19 36 17 25 3 120 순서로 들어온다고 가정해본다.
#### 1) 100 삽입

</br>
<p align="center"><img src=../../img/heap_insert_1.png width=50%></p>

#### 2) 19 삽입(왼쪽부터 저장)

</br>
<p align="center"><img src=../../img/heap_insert_2.png width=50%></p>

#### 3) 36 삽입(왼쪽에 값이 있으므로 오른쪽 노드에 저장)

</br>
<p align="center"><img src=../../img/heap_insert_3.png width=50%></p>

#### 4) 17 삽입
- 100의 양쪽에 값이 저장되어 있으므로 왼쪽 자식 노드의 왼쪽에 저장된다.
- 저장된 후 17은 자신의 부모 노드와 비교하여 작은 경우 그대로 저장되고, 만약 크다면 자신의 부모 노드와 자리를 바꾼다.
- 여기서는 부모 노드가 더 크기때문에 그대로 저장된다.

</br>
<p align="center"><img src=../../img/heap_insert_4.png width=50%></p>

#### 5) 25 삽입
- 마찬가지로 100의 양쪽에 값이 저장되어 있으므로 왼쪽 자식 노드의 오른쪽에 저장된다.
- 여기서 25는 자신의 부모 노드인 19보다 값이 크기 때문에 자리를 바꿔서 저장된다.

</br>
<p align="center"><img src=../../img/heap_insert_5.png width=50%></p>
<p align="center"><img src=../../img/heap_insert_6.png width=50%></p>

#### 6) 3 삽입
- 왼쪽 하단이 모두 채워졌으므로 오른쪽 자식 노드의 왼쪽에 저장된다.

</br>
<p align="center"><img src=../../img/heap_insert_7.png width=50%></p>

#### 7) 120 삽입
- 오른쪽 자식 노드의 오른쪽에 저장된다.
- 120이 자신의 부모 노드보다 크기 때문에 36과 자리를 바꿔서 저장된다.
- 자리를 바꾼후에 다시 부모 노드와 비교해보면 자신의 부모 노드인 100보다 크기 때문에 다시 자리를 바꿔서 저장된다.
- 더이상 비교할 노드가 없으므로 반복이 종료된다.

</br>
<p align="center"><img src=../../img/heap_insert_8.png width=50%></p>
<p align="center"><img src=../../img/heap_insert_9.png width=50%></p>
<p align="center"><img src=../../img/heap_insert_10.png width=50%></p>

### 2. 제거
- 힙에서 값을 제거하면 그 자리를 채우기 위해 마지막 노드를 가져온다.
- 마지막 노드는 채워진 위치에서 자식노드와 비교하면서 자신이 더 작다면 위치를 변경하면서 저장된다.
- 자신의 자식 노드보다 크거나 더이상 비교할 노드가 없으면 비교를 멈춘다.
- 여기서는 힙의 최댓값 120을 제거해본다.

#### 1) 120 제거
- 힙에서 120을 제거한다.

</br>
<p align="center"><img src=../../img/heap_delete_1.png width=50%></p>

#### 2) 마지막 노드 가져오기
- 힙에서 가장 마지막 노드인 36을 120자리에 가져오고, 자신의 자식 노드와 비교한다.
- 왼쪽 자식 노드부터 비교를 시작하고, 여기서는 왼쪽 자식 노드인 25보다 크기 때문에 오른쪽 자식 노드도 비교해본다.
- 오른쪽 자식 노드가 36보다 크기 때문에 위치를 교환해서 저장한다.

</br>
<p align="center"><img src=../../img/heap_delete_2.png width=50%></p>

#### 3) 제거 완료
- 자리를 바꾼 후 다시 자식 노드와 비교한다.
- 현재 자식 노드보다 값이 크기 때문에 비교를 종료하고 제거 동작을 완료한다.

</br>
<p align="center"><img src=../../img/heap_delete_3.png width=50%></p>

<!-- <style>
    @import url(https://fonts.googleapis.com/css?family=Roboto:400,500,700,300,100);

    body {

    font-family: "Roboto", helvetica, arial, sans-serif;
    font-size: 16px;
    font-weight: 400;
    text-rendering: optimizeLegibility;
    }

    div.table-title {
    display: block;
    margin: auto;
    max-width: 600px;
    padding:5px;
    width: 100%;
    }

    .table-title h3 {
    color: #fafafa;
    font-size: 30px;
    font-weight: 400;
    font-style:normal;
    font-family: "Roboto", helvetica, arial, sans-serif;
    text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.1);
    text-transform:uppercase;
    }


    /*** Table Styles **/

    .table-fill {
    background: white;
    border-radius:3px;
    border-collapse: collapse;
    height: 320px;
    margin: auto;
    max-width: 700px;
    padding:5px;
    width: 100%;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
    animation: float 5s infinite;
    }
    
    th {
    color:#D5DDE5;;
    background:#1b1e24;
    border-bottom:4px solid #9ea7af;
    border-right: 1px solid #343a45;
    font-size:23px;
    font-weight: 100;
    padding:24px;
    text-align:left;
    text-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
    vertical-align:middle;
    }

    th:first-child {
    border-top-left-radius:3px;
    }
    
    th:last-child {
    border-top-right-radius:3px;
    border-right:none;
    }
    
    tr {
    border-top: 1px solid #C1C3D1;
    border-bottom-: 1px solid #C1C3D1;
    color:#666B85;
    font-size:16px;
    font-weight:normal;
    text-shadow: 0 1px 1px rgba(256, 256, 256, 0.1);
    align:center;
    }
    
    tr:hover td {
    background:#4E5066;
    color:#FFFFFF;
    border-top: 1px solid #22262e;
    }
    
    tr:first-child {
    border-top:none;
    }

    tr:last-child {
    border-bottom:none;
    }
    
    tr:nth-child(odd) td {
    background:#EBEBEB;
    }
    
    tr:nth-child(odd):hover td {
    background:#4E5066;
    }

    tr:last-child td:first-child {
    border-bottom-left-radius:3px;
    }
    
    tr:last-child td:last-child {
    border-bottom-right-radius:3px;
    }
    
    td {
    background:#FFFFFF;
    padding:20px;
    text-align:left;
    vertical-align:middle;
    font-weight:300;
    font-size:18px;
    text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.1);
    border-right: 1px solid #C1C3D1;
    }

    td:last-child {
    border-right: 0px;
    }

    th.text-left {
    text-align: left;
    }

    th.text-center {
    text-align: center;
    }

    th.text-right {
    text-align: right;
    }

    td.text-left {
    text-align: left;
    }

    td.text-center {
    text-align: center;
    }

    td.text-right {
    text-align: right;
    }
</style> -->