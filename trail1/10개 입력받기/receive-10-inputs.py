arr = list(map(int, input().split()))
sumT = 0
cnt = 0

for i in arr:
    if i == 0:
        break
    sumT += i
    cnt += 1

print(sumT, f'{sumT/cnt:.1f}')