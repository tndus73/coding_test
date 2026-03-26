from collections import deque

def solution(priorities, location):
    
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((p,i))
    count=0
    while queue:
        current = queue.popleft()
        if any (current[0]<q[0] for q in queue):
            queue.append(current)
        else:
            count+=1
            if current[1]==location:
                return count
