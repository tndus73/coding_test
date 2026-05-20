A, B = list(map(int, input().split()))
arr = [0] * B

while A > 1:
    arr[A%B] += 1
    A //= B

sumT = 0
for i in arr:
    sumT += i**2
print(sumT)