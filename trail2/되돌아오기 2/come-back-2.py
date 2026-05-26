commands = input()
x, y = 0, 0
dic = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

answer = -1
time =0

for i in range(len(commands)):
    time += 1
    if commands[i] == 'L':
        dic = (dic+3)%4
    elif commands[i] == 'R':
        dic = (dic+1)%4
    else:
        x = x + dx[dic]
        y = y + dy[dic]

    if x == 0 and y == 0:
        answer = time
        break
print(answer)