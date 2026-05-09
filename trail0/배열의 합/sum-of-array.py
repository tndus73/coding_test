arr = [list(map(int, input().split())) for _ in range(4)]

for row in arr:
    sumT = 0
    for num in row:
        sumT += num
    print(sumT)