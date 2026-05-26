n = int(input())
grid = [input() for _ in range(n)]
k = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# k번 위치에서 들어올 시작 좌표와 방향 정하기
if 1 <= k <= n:
    x = 0
    y = k - 1
    dir_num = 1          # 아래
elif n < k <= 2 * n:
    x = k - n - 1
    y = n - 1
    dir_num = 2          # 왼쪽
elif 2 * n < k <= 3 * n:
    x = n - 1
    y = 3 * n - k
    dir_num = 3          # 위
else:
    x = 4 * n - k
    y = 0
    dir_num = 0          # 오른쪽

cnt = 0

while 0 <= x < n and 0 <= y < n:
    cnt += 1

    if grid[x][y] == '/':
        dir_num = 3 - dir_num
    else:
        dir_num = dir_num ^ 1

    x += dx[dir_num]
    y += dy[dir_num]

print(cnt)