arr = list(map(int, input().split()))

maxT = arr[0]
minT = arr[0]

for i in range(1,len(arr)):
    if arr[i] == 999 or arr[i] == -999:
        break
    if arr[i] > maxT:
        maxT = arr[i]
    if arr[i] < minT:
        minT = arr[i]

print(maxT, minT, end =' ')