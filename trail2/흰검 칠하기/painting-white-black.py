n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

color = [0] * 200000
white = [0] * 200000
black = [0] * 200000

cur = 100000

for num, d in commands:
    num = int(num)

    if d == 'L':
        for i in range(cur, cur - num, -1):
            white[i] += 1
            color[i] = 1
        cur -= num - 1

    else:
        for i in range(cur, cur + num):
            black[i] += 1
            color[i] = 2
        cur += num - 1

    for i in range(200000):
        if white[i] >= 2 and black[i] >= 2:
            color[i] = 3

print(color.count(1), color.count(2), color.count(3))