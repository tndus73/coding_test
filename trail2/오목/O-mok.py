board = [list(map(int, input().split())) for _ in range(19)]

#오른쪽, 아래, 오른쪽 아래, 오른쪽 위(행렬)
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] == 0:
            continue

        for d in range(4):
            cnt = 1
            nx = x
            ny = y

            while True:
                nx += dx[d]
                ny += dy[d]

                if not (0 <= nx < 19 and 0 <= ny < 19):
                    break

                if board[nx][ny] != board[x][y]:
                    break

                cnt += 1
            if cnt == 5:
                print(board[x][y])
                print(x + dx[d] * 2 + 1, y + dy[d] * 2 + 1)
                exit()

print(0)