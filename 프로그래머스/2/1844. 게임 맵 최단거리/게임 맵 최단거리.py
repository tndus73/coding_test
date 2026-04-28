from collections import deque

def solution(maps):
    n = len(maps) #행
    m = len(maps[0]) #열
    
    def bfs(x,y):
        q = deque()
        q.append((0,0))

        dx = [0,1,0,-1]
        dy = [1,0,-1,0]

        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<n and 0<=ny<m:
                    if maps[nx][ny] ==1:
                        maps[nx][ny] = maps[x][y]+1
                        q.append((nx,ny))
                    
    bfs(0,0)
    
    if maps[n-1][m-1] == 1:
        return -1
    return maps[n-1][m-1]