A, B = map(int, input().split())
sumT = 0

for x in range(A, B+1):
    if x % 2 == 0:
        sumT += x
    x += 1
print(sumT)