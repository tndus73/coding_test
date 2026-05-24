offset = 1000
size = 2001

arr = [[0] * size for _ in range(size)]

x1, y1, x2, y2 = [[0] * 3 for _ in range(4)]

for i in range(3):
    x1[i], y1[i], x2[i], y2[i] = map(int, input().split())

for i in range(2):
    for x in range(x1[i]+offset, x2[i]+offset):
        for y in range(y1[i]+offset, y2[i]+offset):
            arr[x][y] = 1

for x in range(x1[2]+offset, x2[2]+offset):
    for y in range(y1[2]+offset, y2[2]+offset):
        arr[x][y] = 0

print(sum(sum(row) for row in arr))
