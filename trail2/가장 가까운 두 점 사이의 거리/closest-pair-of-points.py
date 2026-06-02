n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = 10**18

for i in range(n):
    for j in range(i+1,n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist = (x1-x2)**2 + (y1-y2)**2
        answer = min(answer, dist)
print(answer)