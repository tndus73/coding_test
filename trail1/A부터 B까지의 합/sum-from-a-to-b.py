A, B = map(int, input().split())
sumT = 0
for i in range(A, B+1):
    sumT += A
    A += 1
print(sumT)