from collections import deque
def solution(priorities, location):
    queue = deque()
    for idx, num in enumerate(priorities):
        queue.append((idx, num))
    count = 0
    while queue:
        cur_i, cur_p = queue.popleft()
        if any(cur_p < p for i,p in queue):
            queue.append((cur_i,cur_p))
        else:
            count += 1
            if cur_i == location:
                return count

    
    