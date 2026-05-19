arr = list(map(int, input().split()))
sumT = 0
cnt = 0

for i in arr:
    if i > 250:
        break
    sumT += i
    cnt += 1

print(sumT, round(sumT/cnt,1))
