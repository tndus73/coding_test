board = [list(map(int, input().split())) for _ in range(19)]

#오른쪽, 아래, 오른쪽 아래, 오른쪽 위(행렬)
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] == 0:
            continue

        for d in range(4):
            stones = []
            for k in range(5):
                nx = x + dx[d]*k
                ny = y + dy[d]*k

                if 0 <=nx<19 and 0<=ny<19:
                    stones.append(board[nx][ny])
            
            if len(stones) == 5 and stones.count(board[x][y]) == 5:
                print(board[x][y])
                mid_x = x + dx[d] * 2
                mid_y = y + dy[d] * 2
                print(mid_x + 1, mid_y + 1)
                exit()
print(0)