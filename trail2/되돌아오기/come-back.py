N = int(input())

dx = [1,0,-1,0]
dy = [0,-1,0,1]

dic = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3
}

x, y = 0, 0
time = 0
answer = -1

for _ in range(N):
    dir, dist = input().split()
    dist = int(dist)
    move = dic[dir]

    for _ in range(dist):
        x += dx[move]
        y += dy[move]

        time += 1
        if x==0 and y==0:
            answer = time
            break
    if answer != -1:
        break

print(answer)
