A, B = map(int, input().split())
sumT = 0
arr = []
arr.extend([A, B])
arr.sort()

for x in range(arr[0], arr[1]+1):
    if x % 5 == 0:
        sumT += x
print(sumT)