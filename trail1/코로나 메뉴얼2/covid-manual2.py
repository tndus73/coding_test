arr = [0] * 4

for i in range(3):
    cold, degree = input().split()
    if cold=='Y':
        if int(degree) >= 37:
            arr[0] += 1
        else:
            arr[2] += 1
    else:
        if int(degree) >= 37:
            arr[1] += 1
        else:
            arr[3] += 1

for i in range(len(arr)):
    print(arr[i], end=' ')
if arr[0] >= 2:
    print('E', end=' ')