arr = list(map(int, input().split()))
sumT = 0
cnt = 0

for i in arr:
    if i == 0:
        break
    if i % 2 ==0:
        sumT += i
        cnt +=1

print(cnt, sumT, end =' ')