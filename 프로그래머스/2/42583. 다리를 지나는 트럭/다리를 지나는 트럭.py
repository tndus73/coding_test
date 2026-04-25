from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    
    time = 0
    current_weight = 0
    
    while bridge:
        time += 1
        # 다리에서 맨 앞 빠짐        
        current_weight -= bridge.popleft()
        # 아직 기다리는 트럭이 있으면
        if trucks:
            if current_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)
    return time