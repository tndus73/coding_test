n = int(input())

offset = 100
size = 201

point = [tuple(map(int, input().split())) for _ in range(n)]
arr = [[0] *size for _ in range(size)]

for i, (x1, y1, x2, y2) in enumerate(point):
    if i % 2 == 0:
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr[x][y] = 0 #빨강
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                arr[x][y] = 1 #파랑

print(sum(sum(row) for row in arr))