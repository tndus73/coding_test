N = int(input())
sumT = 0

for x in range(1, N):
    if N % x == 0:
        sumT += x

if sumT == N:
    print('P')
else:
    print('N')

