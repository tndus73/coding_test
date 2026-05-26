n, m = map(int, input().split())

arr = [[0]*m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dic = 0

x, y = 0, 0
arr[x][y] = 1
for i in range(2,n*m+1):
    nx = x + dx[dic]
    ny = y + dy[dic]

    if not(0<=nx<n and 0<=ny<m) or arr[nx][ny] != 0:
        dic = (dic + 1)%4
        nx = x + dx[dic]
        ny = y + dy[dic] 
    
    arr[nx][ny] = i
    x,y = nx, ny

for i in range(n):
    for j in range(m):
        print(arr[i][j], end =' ')
    print()
