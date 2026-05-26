N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = N//2, N//2
dic = 3
answer = board[x][y]

for i in str:
    if i =='R':
        dic = (dic+1)%4
    elif i =='L':
        dic = (dic+3)%4
    else:
        nx = x + dx[dic]
        ny = y + dy[dic]
        if 0<=nx<N and 0<=ny<N:
            x, y = nx, ny
            answer += board[x][y]
print(answer)