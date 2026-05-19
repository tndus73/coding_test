N =int(input())
arr = []

for i in range(1,N+1):
    cnt = 0
    for j in range(2,i+1):
        if i % j == 0:
            cnt +=1
    if cnt == 1:
        arr.append(i)

arr.sort()
print(*arr)