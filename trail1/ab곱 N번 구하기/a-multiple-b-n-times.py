N = int(input())

for i in range(N):
    sumT = 1
    a, b = map(int, input().split())
    for j in range(a, b+1):
        sumT *= j
    print(sumT)
