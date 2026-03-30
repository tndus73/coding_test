from collections import deque
#다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    bridsum = 0
    time = 0

    while trucks or bridsum > 0:
        time += 1
        bridsum -= bridge.popleft()

        if trucks and bridsum + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            bridsum += truck
        else:
            bridge.append(0)

    return time