n = int(input())
point = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    point.append((a, b, c, d))

arr = [[0 for _ in range(1000)] for _ in range(1000)]

for x1, y1, x2, y2 in point:
    for x in range(x1,x2):
        for y in range(y1,y2):
            arr[x][y] = 1

sumT = 0

for row in arr:
    for i in row:
        sumT += i
print(sumT)

# Please write your code here.