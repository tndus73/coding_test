arr = [ list(map(int, input().split())) for _ in range(4)]
sumT = 0
for i in range(4):
    for j in range(i+1):
        sumT += arr[i][j]
print(sumT)
