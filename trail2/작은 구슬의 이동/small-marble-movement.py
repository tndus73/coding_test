n, t = map(int, input().split())
r, c, d = input().split()
x, y = int(r)-1, int(c)-1

dx = [0, 1, -1, 0]
dy = [1, 0 , 0, -1]

dic = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = dic[d]

for _ in range(t):
    nx = x + dx[move_dir]
    ny = y + dy[move_dir]

    if 0 <= nx < n and 0 <= ny < n:
        x, y = nx, ny
    else:
        move_dir = 3- move_dir
print(x+1,y+1)



