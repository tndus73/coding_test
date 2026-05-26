n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

x, y = 0, 0
move_dir = 0 # 오른쪽

arr[0][0] = 1

for i in range(2, n*m+1):
    nx = x + dx[move_dir]
    ny = y + dy[move_dir]

    if not (0<=nx<n and 0<=ny<m) or arr[nx][ny] != 0:
        move_dir = (move_dir + 1) % 4
        nx = x + dx[move_dir]
        ny = y + dy[move_dir]

    arr[nx][ny] = i
    x, y = nx, ny

for i in range(n):
    for j in range(m):
        print(arr[i][j], end =' ')
    print()