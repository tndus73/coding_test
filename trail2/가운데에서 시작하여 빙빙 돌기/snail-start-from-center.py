n = int(input())
grid = [[0] * n for _ in range(n)]

x, y = n//2, n//2
grid[x][y] = 1

dir = 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


for i in range(2,n*n+1):
    x += dx[dir]
    y += dy[dir]

    grid[x][y] = i
    next_dir = (dir+1)%4

    nx = x + dx[next_dir]
    ny = y + dy[next_dir]

    if 0<=nx<n and 0<=ny<n and grid[nx][ny] == 0:
        dir = next_dir

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
# Please write your code here.
