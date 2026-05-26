n, m = map(int, input().split())

arr = [[0]*n for _ in range(n)]

dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    x, y = x-1, y-1
    cnt = 0
    arr[x][y] = 1

    for dic in range(4):
        nx = x + dx[dic]
        ny = y + dy[dic]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 1:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)
