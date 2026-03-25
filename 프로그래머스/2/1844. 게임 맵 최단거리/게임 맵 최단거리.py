from collections import deque


def solution(maps):
    n = len(maps) #행
    m = len(maps[0]) #열
    
    def bfs(y,x):
        #큐
        q = deque() 
        q.append((0, 0))

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        
        while q:
            y, x = q.popleft()
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if 0<=ny<n and 0<=nx<m:
                    if maps[ny][nx] == 1:
                        maps[ny][nx] = maps[y][x] + 1
                        q.append((ny,nx))
    bfs(0,0)
    
    if maps[n-1][m-1] == 1:
        return -1
    return maps[n-1][m-1]
