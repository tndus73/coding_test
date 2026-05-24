offset = 1000
size = 2002

points = [tuple(map(int, input().split())) for _ in range(2)]

arr = [[0] * size for _ in range(size)]

x1, y1, x2, y2 = points[0]
for x in range(x1+offset, x2+offset):
    for y in range(y1+offset, y2+offset):
        arr[x][y] = 1

x1, y1, x2, y2 = points[1]
for x in range(x1+offset, x2+offset):
    for y in range(y1+offset, y2+offset):
        arr[x][y] = 0

min_x = size
max_x = -1
min_y = size
max_y = -1

for x in range(size):
    for y in range(size):
        if arr[x][y] == 1:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

if max_x == -1:
    print(0)
else:
    print((max_x-min_x+1)*(max_y-min_y+1))