n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

offset = 100
size = 2001

arr = [[0]*size for _ in range(size)]

for x, y in points:
    x = x + offset
    y = y + offset
    for i in range(x, x+8):
        for j in range(y, y+8):
            arr[i][j] = 1

print(sum(sum(row) for row in arr))
