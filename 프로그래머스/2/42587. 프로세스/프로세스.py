from collections import deque

def solution(priorities, location):
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((p,i))
    
    count = 0
    while queue:
        cur_p, cur_i = queue.popleft()
        
        if any(cur_p < p for p, _ in queue):
                queue.append((cur_p, cur_i))
        else:
                count += 1
                if cur_i ==location:
                    return count
    
    