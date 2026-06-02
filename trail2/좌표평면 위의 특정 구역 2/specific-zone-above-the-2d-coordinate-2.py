n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = []

for i in range(n):
    xs = []
    ys = []
    for j in range(n):
        if i == j:
            continue
        else:
            xs.append(points[j][0])
            ys.append(points[j][1])
    answer.append((max(xs)-min(xs))*(max(ys)-min(ys)))

print(min(answer))