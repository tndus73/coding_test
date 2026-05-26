n, m = map(int, input().split())

arr = [[0]*m for _ in range(n)]
# A : 65 Z : 90
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

move = 0
x, y = 0, 0
arr[x][y] = 'A'

for i in range(1, n*m):

    nx = x + dx[move]
    ny = y + dy[move]

    if not(0<=nx<n and 0<=ny<m) or arr[nx][ny] != 0:
        move = (move+1)%4
        nx = x + dx[move]
        ny = y + dy[move]

    arr[nx][ny] = chr(65+(i%26))
    x, y = nx, ny

for i in range(n):
    for j in range(m):
        print(arr[i][j], end =' ')
    print()
     