n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    x1, x2 = lines[i]
    overlap = False

    for j in range(n):
        if i == j:
            continue
        y1, y2 = lines[j]

        if (x1<y1 and x2>y2) or (x1>y1 and x2<y2):
            overlap = True
            break
    
    if not overlap:
        answer += 1

print(answer)
    
