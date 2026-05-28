n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = 10**18

for skip in range(1, n-1):
    total = 0
    prev = 0
    for i in range(1,n):
        if i == skip:
            continue
        x1, y1 = points[prev]
        x2, y2 = points[i]

        total += abs(x1-x2)+abs(y1-y2)
        prev = i
    answer = min(answer, total)

print(answer)

# Please write your code here.