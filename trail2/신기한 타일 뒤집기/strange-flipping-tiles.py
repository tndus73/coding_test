n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

point = [0] * 20000
cur = 10000
for num, direction in commands:
    num = int(num)
    if direction == 'R':
        for i in range(cur, cur+num):
            point[i] = 1
            #검은색
        cur = cur + num -1

    else:
        for i in range(cur, cur-num,-1):
            point[i] = 2
            #흰색
        cur = cur - num +1

print(point.count(2), point.count(1), end= ' ')

# Please write your code here.