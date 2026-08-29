from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    bridge = deque()
    total = 0
    while q or bridge:
        answer += 1
        while bridge and bridge[0][0] <= answer:
            total -= bridge.popleft()[1] 
            
        if not q or total + q[0] > weight:
            continue
        
        x = q.popleft()
        bridge.append((answer + bridge_length, x))
        total += x
        
    return answer
