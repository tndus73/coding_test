N = int(input())

for i in range(N):
    sumT = 0
    a, b = map(int, input().split())
    for j in range(a, b+1):
        if j % 2 == 0:
            sumT += j
    print(sumT)