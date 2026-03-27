from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    bridge_sum = 0
    time = 0

    while trucks or bridge_sum > 0:
        time += 1
        bridge_sum -= bridge.popleft()

        if trucks and bridge_sum + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            bridge_sum += truck
        else:
            bridge.append(0)

    return time